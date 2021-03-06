#!/usr/bin/env python
""" MultiQC gatkdoc plugin functions
"""

from __future__ import print_function
from pkg_resources import get_distribution
import logging

from multiqc.utils import report, util_functions, config

# Initialise the main MultiQC logger
log = logging.getLogger('multiqc')

# Save this plugin's version number (defined in setup.py) to the MultiQC config
config.gatkdoc_plugin_version = get_distribution("multiqc_gatkdoc_plugin").version


# Add default config options for the things that are used in MultiQC_NGI
def gatkdoc_plugin_execution_start():
    """ Code to execute after the config files and
    command line flags have been parsedself.

    This setuptools hook is the earliest that will be able
    to use custom command line flags.
    """

    # Halt execution if we've disabled the plugin
    if config.kwargs.get('disable_plugin', True):
        return None

    log.info("Running GATK DepthOfCoverage MultiQC Plugin v{}".format(config.gatkdoc_plugin_version))

    # Add to the main MultiQC config object.
    # User config files have already been loaded at this point
    #   so we check whether the value is already set. This is to avoid
    #   clobbering values that have been customised by users.

    # Add to the search patterns used by modules
    if 'gatkdoc/key_value_pairs' not in config.sp:
        config.update_dict( config.sp, { 'gatkdoc/key_value_pairs': { 'fn': '*.sample_summary' } } )

    # Some additional filename cleaning
    config.fn_clean_exts.extend([
        '.depthOfCov.COUNT_READS',
    ])
