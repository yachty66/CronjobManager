import os

if __name__ == "__main__":
    command = "python3 /Users/maxhager/Projects2022/CronjobManager/createCronjobs.py"
    os.popen("sudo -S %s"%(command), 'w').write('password')




