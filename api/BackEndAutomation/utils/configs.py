import configparser
import os


def getConfig():
    config = configparser.ConfigParser()
    config.read("utils\\properties.ini")
    return config


def getPassword():
    password = os.environ.get('GPASS')
    return password
