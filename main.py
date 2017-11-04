#/usr/bin/python

import logging
from config import *
import argparse
import datetime
from source import *


parser = argparse.ArgumentParser(description='Extract details from a link and store')
parser.add_argument('--config', type=str, nargs=1, required=True, dest='configFile',
                    help='Config file path/by default searches in the present directory')
parser.add_argument('--logfile', type=str, nargs=1, required=True, dest='logFile',
                    help='log file path/by default in the present directory')

args= parser.parse_args()
CONFIG_FILE = args.configFile[0]
LOG_FILE = args.logFile[0]

# enable info logs
logging.basicConfig(
    format="%(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s",
    filename='LOG_FILE',
    level=logging.INFO )

def main():
	config = Config(CONFIG_FILE)
	print config.getSourceClass()
	sourceClassName = eval(config.getSourceClass())
	sourceObj = sourceClassName( config.getLink())
	pageDetails = sourceObj.extractData()
	pageDetails["time"] = datetime.datetime.now()

	print pageDetails

if __name__ == "__main__":
    # execute only if run as a script
    main()
