import configparser
import os

import mysql.connector
import paramiko as par
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


def getSSHConnection():
    host = getConfig()['SSH']['host']
    port = getConfig()['SSH']['port']
    user = getConfig()['SSH']['user']
    password = getConfig()['SSH']['password']
    try:
        ssh = par.SSHClient()  # creates a stream of connection
        ssh.set_missing_host_key_policy(par.AutoAddPolicy)  # supress checking of ssh key
        ssh.connect(host, port, user, password)
        ssh.exec_command('ls', timeout=5)
        return ssh
    except Exception as e:
        print("Connection lost : %s" % e)
