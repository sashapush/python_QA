import paramiko
import paramiko as par

from api.BackEndAutomation.utils.configs import getConfig

host = getConfig()['SSH']['host']
port = getConfig()['SSH']['port']
user = getConfig()['SSH']['user']
password = getConfig()['SSH']['password']
ssh = par.SSHClient()  # creates a stream of connection
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # supress checking of ssh key
ssh.connect(host, port, user, password)
print("Connection was done")
ssh.close()
