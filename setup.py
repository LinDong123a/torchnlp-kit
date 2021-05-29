#!/usr/bin/env python 3.6
import os
from setuptools import setup, find_packages


with open('README.md', "r", encoding="utf-8") as rfile:
    long_description = rfile.read()

with open(os.path.join("torchnlp-kit", "__about__.py")) as rfile:
    v_dict = {}
    exec(rfile.read(), v_dict)
    version = v_dict['__version__']


setup_info = dict(
    # Metadata
    name="torchnlp-kit",
    version=version,
    author="Dongsheng Lin",
    author_email="lds354449275@gmail.com",
    url="https://github.com/LinDong123a/torchnlp-kit",
    description="Lightweight extends for pytorch nlp",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='pytorch nlp text torchtext torchnlp extends',
    python_requires='>=3.6',

    # Package info
    packages=find_packages(exclude=['.vscode', 'build_tools', 'docs', 'tests']),
    zip_safe=True,
)

setup(**setup_info)
