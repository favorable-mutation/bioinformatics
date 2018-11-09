#!/usr/bin/env python2.7

# TODO
# - add optional args to allow input and output directory specification
# - add short arg options (e.g. "-t, --time" produce the same result)

import os
import sys
import time
import datetime
import argparse

parser = argparse.ArgumentParser(description="Data transfer from polara to Brown lab file server\nPlease run this from directory you wish to transfer files from")
parser.add_argument("--time", type=int, required=True,
     help="Runtime of data collection in hours - Required")

args = parser.parse_args()
cwd = os.getcwd()
ext = "*.tif"
copy_endtime = time.time() +3600 * (args.time)


while time.time() < copy_endtime:
	os.system("rsync -hurvza --progress --remove-source-files `find {cwd} -type f -name '{ext:s}' -mmin +5` adrian@10.119.49.163:/media/file_server/Polara_Data/".format(cwd=cwd, ext=ext))
	time.sleep(60)
print "\nPolara data transfer completed"

