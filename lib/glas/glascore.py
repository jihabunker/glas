
import os as os
import logging as log
import configparser as CP
import MySQLdb as mc
import string as string
import sys as sys

GLASHOME = os.environ['GLAS_HOME']
logconfigfile = GLASHOME+'/conf/glas.conf'


class gcore:
    CFG_DBHOST=0
    CFG_DBUSER=0
    CFG_DBPASS=0
    CFG_LOG_FORMAT=0
    CFG_LOG_LEVEL=0
    fd = 0
    dbcon = 0
    logger = 0
    loggerfile = 0
    loggerstream = 0
    def __init__(self):
        cfg = CP.ConfigParser()
        cfg.read(logconfigfile)
        self.CFG_DBHOST = cfg.get('DB','hostname')
        self.CFG_DBUSER = cfg.get('DB','username')
        self.CFG_DBPASS = cfg.get('DB','password')
        self.CFG_DBNAME= cfg.get('DB','dbname')

        logformat   = log.Formatter('%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s  > %(message)s')
        fileHandler = log.FileHandler(cfg.get('LOGGING','log_file'))
        streamHandler = log.StreamHandler()
        fileHandler.setFormatter(logformat)
        streamHandler.setFormatter(logformat)

        self.logger = log.getLogger("loganalysislog")
        self.logger.addHandler(fileHandler)
        self.logger.addHandler(streamHandler)
        self.logger.setLevel(cfg.get("LOGGING","log_level").upper())
        self.result = 0


    def mysqlcon(self):
        #print (self.CFG_DBHOST)
        #print (self.CFG_DBUSER)
        #print (self.CFG_DBPASS)
        #print (self.CFG_DBNAME)
        try:
            self.dbcon = mc.connect(host=self.CFG_DBHOST, user=self.CFG_DBUSER, passwd=self.CFG_DBPASS, db=self.CFG_DBNAME)
            self.logger.info('db connect success')
        except mc.Error as e:
            self.logger.critical(e.args[1])
            sys.exit(1)

        return self.dbcon
