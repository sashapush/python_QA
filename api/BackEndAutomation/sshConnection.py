import csv

import paramiko as par

from api.BackEndAutomation.utils.configs import getConfig
from api.BackEndAutomation.utils.configs import getSSHConnection

# Start connection
ssh = getSSHConnection()
print("Connection was started successfully")
# Run commands
# stdin, stdout, stderr = ssh.exec_command("ls -a") #Paramiko object
stdin, stdout, stderr = ssh.exec_command("cat demo.txt")
# print(stdout.readlines()) should be commented since it'll conflict with .readLines() below
print(stderr.readlines())
lines = stdout.readlines()
print(lines[1])

# Upload file from machine to remote server
sftp = ssh.open_sftp()
# Todo refactor into send method
remotePath = "script.py"
localPath = "C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\api\\BackEndAutomation\\batch\\script.py"
sftp.put(localPath, remotePath)

remotePath = "loanasa.csv"
localPath = "C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\api\\BackEndAutomation\\batch\\loanasa.csv"
sftp.put(localPath, remotePath)

# Execute script on remote host
stdin, stdout, stderr = ssh.exec_command("python script.py")

# Download file to local system
remotePath = "/home/ec2-user/loanasa.csv"
localPath = "C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\api\\BackEndAutomation\\batch\\loanasa.csv"
sftp.get("loanasa.csv", "C:\\Users\\Alex\\PycharmProjects\\pythonAQAdraft\\api\\BackEndAutomation\\batch\\output"
                        "\\loanasa.csv")
ssh.close()

# Parse output
with open("batch\\output\\loanasa.csv", "r") as csvFile:
    Obj = csv.reader(csvFile, delimiter=",")
    for row in Obj:
        print(row)
        if row[0] == "32321":
            print("ASS", row[1], "ASS")
