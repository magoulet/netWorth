import MySQLdb
import os
import yaml

# Configure db
curPath = os.path.dirname(os.path.abspath(__file__))

conf = yaml.load(open(curPath+'/db.yaml'),Loader=yaml.FullLoader)

def connection(dbName):
    conn = MySQLdb.connect(host=conf['mysql_host'],
                           user = conf['mysql_user'],
                           passwd = conf['mysql_password'],
                           db = dbName)
    c = conn.cursor()

    return c, conn
