# -*- coding: utf-8 -*-
import sys
import re
from time import strftime, localtime

# -- Glas core class -- #
from lib.glas.glascore import gcore

curYear = strftime("%Y", localtime())
eventCountArray = {}

regex_application = r'.*?\['
regex_obj = re.compile(regex_application,re.DOTALL)

gc = gcore()
dbcon = gc.mysqlcon()

# Input is from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input from the mapper
    event, count = line.split('\t', 1)
    # Cast count to int
    try:
        count = int(count)
    except ValueError:
        continue

    # Compute event count
    try:
        eventCountArray[event] = eventCountArray[event]+count
    except:
        eventCountArray[event] = count

# Write the results (unsorted) to stdout
for event in eventCountArray.keys():
    event = event.strip()
    #spline[0] : month
    #spline[1] : node
    #spline[2] : application
    #spline[3] : message
    spline = event.split('==')
    appsName = ""
    try :
        match = re.search(regex_application, spline[2])
        appsName = match.group(0)
    except AttributeError:
        appsName = spline[2]

    ## TODO 
    ## check log message is error / warning/ normal  
    ## if error / warning then this logic can check what is exact mean from stackoverflow
    ## create new table for result from stackoverflow and connect error msg ID(logrows table)  and answer ID(answer table)
    ## 
    c=dbcon.cursor()
    sql = "insert into logrows (year, month, node, application, message, cnt) values (%s,%s,%s,%s,%s,%s)"
    c.execute(sql , (curYear,spline[0],spline[1], appsName[:-1], spline[3], eventCountArray[event]))

dbcon.commit()
dbcon.close()
