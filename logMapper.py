
import sys as sys
import re as re
import os as os


#-- include kernel message --#
#data_pattern = r"(\w+)\s+(\d+)\s+(\d+:\d+:\d+)\s+(\w+\W*\w*)\s+(.*?\:)\s+(\[.*\])\s+(.*$)"
#-- exclude kernel message --#

data_pattern = r"(\w+)\s+(\d+)\s+(\d+:\d+:\d+)\s+(\w+\W*\w*)\s+(.*?\:)\s+(.*$)"
regex_obj = re.compile(data_pattern, re.VERBOSE)

#filepath = os.environ["Data/*/*/*/*"]
#filename = os.path.split(filepath)[-1]
#file = "/var/log/messages.1"

# --- get all lines from data file ---

#f = open (file, "r")
#lines = f.readlines()

#for strLineRead in lines:
for strLineRead in sys.stdin:

    # --- remove leading and trailing whitespace ---
    strLineRead = strLineRead.strip()

    # --- split the line into fields ---
    parsed_log = ""
    parsed_log = regex_obj.search(strLineRead)

    if parsed_log:
        s = parsed_log.group(1)+"-"+parsed_log.group(2)+"-"+parsed_log.group(3)+"-"+parsed_log.group(4)+"-"+parsed_log.group(5)
        print ('%s\t%s\t%s' % (s, parsed_log.group(6), "1"))
    else:
        print ('%s' % (strLineRead));
        print ("none")
