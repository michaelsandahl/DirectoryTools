import os
from os.path import join
import shutil
import glob
import configparser

# A list of the main directories which contain all Projects
MAIN_DIRS = ('Archived', 'Current')
###############################################################################
# A regex to match any year from 1900-2099
# d_year = re.compile('(19|20)\d\d')
###############################################################################

###############################################################################
# Config Stuff
###############################################################################

config = configparser.Configparser()

def archive():
    '''Create & populate archive directory

    Checks for the presence of an archive folder, and creates
    the folder if it doesn't exist. Moves any archive files into
    the archive directory.'''

    # Check for archive folder first
    archive_dir = false;


def check_dir(dirs):
    '''Checks the current working directory

    Returns True for any directories passed to the method'''
    if os.path.basename(os.getcwd()) in dirs:
        print(os.path.basename(PROJ_DIR))
        return True
    else:
        return False
