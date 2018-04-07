# -*- coding:utf-8 -*-

import sys
import re
import os
import codecs
from time import localtime, strftime

# -- Glas core class -- #
from lib.glas.glascore import gcore
gc = gcore()
# -- syslog pattern --#
data_pattern = r"(\w+)\s+(\d+)\s+(\d+:\d+:\d+)\s+(\w+\W*\w*)\s+(.*?\:)\s+(.*$)"
# ---
# group(1) : Month
# group(2) : Date
# group(3) : Time
# group(4) : hostname
# group(5) : Application
# group(6) : Message
# ---
regex_obj = re.compile(data_pattern, re.VERBOSE)
curDate = strftime("%Y%m%d", localtime())
#filepath = os.environ["Data/*/*/*/*"]
#filename = os.path.split(filepath)[-1]
#file = "/var/log/messages.1"

# --- get all lines from data file ---

#f = open (file, "r")
#lines = f.readlines()

sucsFile = gc.CFG_DATADIR+"/success_"+curDate+".log"
failFile = gc.CFG_DATADIR+"/failed_"+curDate+".log"

pfHandler = open(sucsFile, "w")
rfHandler = open(failFile, "w")

gc = gcore()
#for strLineRead in lines:
procLine = 0
procHostname = ""
for strLineRead in sys.stdin:

    # --- remove leading and trailing whitespace ---
    strLineRead = strLineRead.strip()

    # --- split the line into fields ---
    parsed_log = ""
    parsed_log = regex_obj.search(strLineRead)

    if parsed_log:
        s = parsed_log.group(1)+"=="+parsed_log.group(2)+"=="+parsed_log.group(3)+"=="+parsed_log.group(4)+"=="+parsed_log.group(5)
        if parsed_log.group(6) != '':
            print ('{0}=={1}=={2}=={3}\t{4}'.format(parsed_log.group(1), parsed_log.group(4), parsed_log.group(5),parsed_log.group(6), "1"))
            pfHandler.write(strLineRead+'\n')
        else:
            rfHandler.write(strLineRead+'\n')

    else:
        #print ('%s' % (strLineRead));
        rfHandler.write(strLineRead+'\n')
    procLine += 1

logStr = str("Success : %d\n" % procLine)
gc.logger.info(logStr)
pfHandler.close()
rfHandler.close()
