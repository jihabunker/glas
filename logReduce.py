# -*- coding: utf-8 -*-
import sys

from time import strftime, localtime
sys.path.append('lib/glas')

# -- Glas modules --
import glascore

curYear = strftime("%Y", localtime())
eventCountArray = {}

gc = glascore.gcore()
dbcon = gc.mysqlcon()

# Input is from STDIN
for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()

    # Parse the input from the mapper
    try:
        event, count = line.split('\t', 1)
    except ValueError:
        pass

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
    spline = event.split('-')
    #print ('%s\t%s\t%s'% ( curYear, event, eventCountArray[event] )
    c=dbcon.cursor()
    sql = str("""insert into logrows (year,month,message,cnt) values ("%s","%s","%s",%d)""" % (curYear,spline[0],spline[1],int(eventCountArray[event],)))
    sql = "insert into logrows (year, month, message, cnt) values (%s,%s,%s,%s)"
    c.execute(sql , (curYear,spline[0],spline[1],eventCountArray[event]))

dbcon.commit()
dbcon.close()
