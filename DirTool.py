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
# Begin Config Stuff

config = configparser.Configparser()
config.read('directorytools.ini')
# Access the Mill Creek section of the config file
millcreek = config['MillCreek']

# TODO: Add in config file handling code.  Also figure out what exactly we want to put into
# the config file, and whether we want to be able to change it.

# End Config Stuff
###############################################################################

###############################################################################
# Logging Stuff

# Log file
LOG_FILE = config.

# create logger
logger = logging.getLogger("HouseClean")
logger.setLevel(logging.INFO)

# create file handler and set level to debug
fh = logging.FileHandler(LOG_FILE)
fh.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter(
    fmt = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = '%a, %d %b %Y %H:%M:%S'
    )

# add formatter to ch
fh.setFormatter(formatter)

# add fh to logger
logger.addHandler(fh)

# End Logging Stuff
###############################################################################

# Check for archive folder
def archive_check(dirname):
    '''Check for an archive directory in the project folders

    Create one if it does not exist'''
    if 'archive' not in os.listdir(dirname):
        archive = os.path.join(root, 'archive')
        os.mkdir(archive)
    else:
        pass

def pdf_check(dirname):
    '''Check for a pdf directory in the project folders

    Create one if it does not exist'''
    if 'pdf' not in os.listdir(dirname):
        pdf = os.path.join(root, 'pdf')
        os.mkdir(pdf)
    else:
        pass

def clean_dir(dirname):
    '''Search through the directory for temporary files

    Delete those files older than 14 days'''
    for files in dirname:
        # See if they match the files_to_remove extensions
            # If they are less than 14 days old leave them alone
            # Otherwise remove them
        # Otherwise see if they match the files_to_keep extensions
            # Figure out what to do here. Should we put them into a list, and
            # return that list to be handled by another module, or just handle all
            # of that here?
    pass

