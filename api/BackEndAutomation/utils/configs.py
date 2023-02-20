import configparser
import os

import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read("C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\api\\BackEndAutomation\\utils\\properties.ini")
    return config


db_connect_config = {
    "host": getConfig()['SQL']['host'],
    "database": getConfig()['SQL']['database'],
    "user": getConfig()['SQL']['user'],
    "password": getConfig()['SQL']['password']
}


def getPassword():
    password = os.environ.get('GPASS')
    return password


def getDbConnection():
    try:
        conn = mysql.connector.connect(**db_connect_config)
        if conn.is_connected():
            print("Connection established successfully")
            return conn
    except Error as e:
        print(e)


def getQuery(query):  # can also be placed in configs
    c = getDbConnection()
    cursor = c.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    c.close()
    return row

def sendFileSSH(remotePath, localPath, sftp):
    remotePath = remotePath
    localPath = localPath
    return sftp.put(localPath, remotePath)
