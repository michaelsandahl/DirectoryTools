###############################################################################
# A maintainence script that will check for 'mailer' dwg & pdf files
# starting from the directory where the command is callled.  The found
# files have a shortcut created and placed into the appropriate folder
#
# Author: Michael Sandahl
# Created: 12-31-2013
# Version: 0.1
###############################################################################

import os
from os.path import join
import fnmatch
import sys
import winshell

###############################################################################
# Global variables
###############################################################################
# The directory that the script is run from
START_DIR = os.getcwd()

###############################################################################
# Methods
###############################################################################

def find_mailer():
    '''Find the mailer files

    Then do something with them'''

    # A container for the mailer pdfs we find
    mailer_pdf = []
    mailer_dwg = []
    # This is the ending of the file we are trying to match
    pdf_match = '*mailer.pdf'
    dwg_match = '*mailer.dwg'
    # Start from the bottom of the curr_dir to look for files
    # When we find a match we add it to the mailers container
    for root, dirs, files in os.walk(START_DIR, topdown = False):
        for name in files:
            if fnmatch.fnmatch(name, pdf_match):
                mailer_pdf.append(os.path.join(root, name))
            elif fnmatch.fnmatch(name, dwg_match):
                mailer_dwg.append(os.path.join(root, name))
            else:
                pass

    return mailer_pdf, mailer_dwg

def create_shortcut(path, target):
    shortcut = winshell.shortcut(target)
    shortcut.write(path)

###############################################################################
# Main
###############################################################################

def main():
    mailer_pdf_dir = r"C:\Users\Public\Documents\MillCreekDesign\Standard Plans\Mailers\PDF"
    mailer_dwg_dir = r"C:\Users\Public\Documents\MillCreekDesign\Standard Plans\Mailers\DWG"

    # print ('Start =', START_DIR)
    pdf_mailers = 0
    dwg_mailers = 0
    mailer_list = find_mailer()

    for mailer in mailer_list[0]:
        # wDir = os.path.dirname(mailer)
        target = mailer
        filename = os.path.basename(mailer)
        path = os.path.join(mailer_pdf_dir, filename[:-4] + '.lnk')

        create_shortcut(path, target)
        pdf_mailers += 1

    for mailer in mailer_list[1]:
        # wDir = os.path.dirname(mailer)
        target = mailer
        filename = os.path.basename(mailer)
        path = os.path.join(mailer_dwg_dir, filename[:-4] + '.lnk')


        create_shortcut(path, target)
        dwg_mailers += 1

    print(pdf_mailers, 'PDF mailer shortcuts &', dwg_mailers, 'DWG mailer shortcuts\n')
    print('were updated in the following directory\n')
    print(mailer_pdf_dir)

    input('\nHit Enter to quit')
    sys.exit()
# Run the program
main()

if __name__ == '__main__':
	main()
