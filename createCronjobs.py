import subprocess

def writeInCrontab():
    subprocess.run("crontab -l > /Users/maxhager/Projects2022/CronjobManager/temp", shell=True)
    with open("temp", "w") as f:
        f.write("")
    subprocess.run("crontab /Users/maxhager/Projects2022/CronjobManager/temp", shell=True)
    subprocess.run("crontab /Users/maxhager/Projects2022/CronjobManager/Cronjobs.txt", shell=True)
    
        
if __name__ == "__main__":
    writeInCrontab()

