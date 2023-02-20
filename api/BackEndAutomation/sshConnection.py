import paramiko
import paramiko as par

from api.BackEndAutomation.utils.configs import getConfig

# Start connection
host = getConfig()['SSH']['host']
port = getConfig()['SSH']['port']
user = getConfig()['SSH']['user']
password = getConfig()['SSH']['password']
ssh = par.SSHClient()  # creates a stream of connection
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)  # supress checking of ssh key
ssh.connect(host, port, user, password)
print("Connection was done")
# Run commands
# stdin, stdout, stderr = ssh.exec_command("ls -a") #Paramiko object
stdin, stdout, stderr = ssh.exec_command("cat demo.txt")

# print(stdout.readlines()) should be commented since it'll conflict with .readLines() below
print(stderr.readlines())
lines = stdout.readlines()
print(lines[1])
ssh.close()
