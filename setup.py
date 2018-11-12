#!/usr/bin/env python
"""
GATK DepthOfCoverage plugin for MultiQC.
For more information about MultiQC, see http://multiqc.info
"""

from setuptools import setup, find_packages

version = '1.1'

setup(
    name = 'multiqc_gatkdoc_plugin',
    version = version,
    author = 'Matteo Massidda',
    author_email = 'matteo.massidda@crs4.it',
    description = "GATK DepthOfCoverage MultiQC plugin",
    long_description = __doc__,
    keywords = 'bioinformatics',
    url = 'https://bitbucket.org/massiddaMT/gatkdoc_plugin',
    license = '###',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'multiqc'
    ],
    entry_points = {
        'multiqc.modules.v1': [
            'gatkdoc = gatkdoc_plugin:MultiqcModule',
        ],
        'multiqc.cli_options.v1': [
            'disable_plugin = gatkdoc_plugin.cli:disable_plugin'
        ],
        'multiqc.hooks.v1': [
            'execution_start = gatkdoc_plugin.custom_code:gatkdoc_plugin_execution_start'
        ]
    },
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: JavaScript',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
