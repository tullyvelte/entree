'''
.. module:: entree.projects.flask_large
.. moduleauthor:: Julien Spronck
.. created:: Feb 2018

Module for large Flask projects
'''

import os
from entree.projects.base import ProjectBase

__version__ = '0.0'

_, FILEBASE = os.path.split(__file__)

PROJECT_TYPE = os.path.splitext(FILEBASE)[0]
TEMPLATE_DIR = 'python-flask-large'
REPLACE = {
    'unittest_py.template': 'test_{{ modname }}.py',
    'src': '{{ modname }}'
}


class FlaskLarge(ProjectBase):
    '''Class for large Flask projects

    Class attributes:
        project_type (str): project type (e.g. flask)
        template_dir (str): path to the project template directory relative to
            the template root directory
        common_dir (str): path to the common template directory relative to
            the template root directory
        single_file (str): path to a single file that you want to create in
            single-file mode relative to the template root directory
        replace (dict, default=None): dictionary mapping template file
            names that should be replaced when creating the files. For
            example, {'unittest_py.template': 'test_project.py'}
        version (str): version number
    '''
    project_type = PROJECT_TYPE
    template_dir = TEMPLATE_DIR
    replace = REPLACE
    version = __version__
