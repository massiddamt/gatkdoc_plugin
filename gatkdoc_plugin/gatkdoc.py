#!/usr/bin/env python

""" MultiQC gatkdoc plugin module """

from __future__ import print_function
from collections import OrderedDict
import logging
from multiqc import config
from multiqc.plots import linegraph
from multiqc.modules.base_module import BaseMultiqcModule

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

class MultiqcModule(BaseMultiqcModule):

    def __init__(self):

        # Halt execution if we've disabled the plugin
        if config.kwargs.get('disable_plugin', True):
            return None

        # Initialise the parent module Class object
        super(MultiqcModule, self).__init__(
            name = 'GATK DepthOfCoverage',
            target = "gatkdoc",
            anchor = 'gatkdoc',
            href = 'https://bitbucket.org/massiddaMT/gatkdoc_plugin',
            info = " is a plugin for GATK DepthOfCoverage output inclusion in the MultQC report."
        )

        # Find and load any input files for this module
        self.gatkdoc_data = dict()
        headers = OrderedDict()

        for f in self.find_log_files('gatkdoc/key_value_pairs'):
            self.gatkdoc_data[f['s_name']] = dict()
            for l in f['f'].splitlines():
                key=l.split("\t", 1)[0]
                value=l.split("\t", 3)[2]
                self.gatkdoc_data[f['s_name']][key] = value
            headers[key] = {
                'title': 'GATK_DOC - Avg Cov',
                'description': 'Average Coverage computed by GATK DepthOfCoverage',
                'min': 0,
                'scale': 'RdYlGn-rev',
                'format': '{:,.2f}'
            }
        self.general_stats_addcols(self.gatkdoc_data, headers)

        # Filter out samples matching ignored sample names
        self.gatkdoc_data = self.ignore_samples(self.gatkdoc_data)

        # Nothing found - raise a UserWarning to tell MultiQC
        if len(self.gatkdoc_data) == 0:
            log.debug("Could not find any reports in {}".format(config.analysis_dir))
            raise UserWarning

        log.info("Found {} reports".format(len(self.gatkdoc_data)))

        # Write parsed report data to a file
        self.write_data_file(self.gatkdoc_data, 'multiqc_gatkdoc')



