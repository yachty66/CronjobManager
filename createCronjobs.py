'''
Notes:
    - it unpractically trying to manage crontab with python because If it is more effiecient to write directly something into a file 
    - I could create a text file which i could use to create a cronjob. always if i update the file i run a py script which will write its content into cronjob
    can i figure out if a cronjob was running just by checking with >>? Or does it just show me print results. Of course it does show me print results but an error would be also a print result.
    
    cronjobs which I need:
    shortcuts on reeboot - 
    email daily aber das muss ich noch erstellen
    clean screens and downloads every sunday 12 
    update paper every day at 12
    
    if print star
    
    
- [x] create python file which adds a line with a string to a txt file when executed 
- [x] try to create a cronjob with python which executes this file every minute
- [x] create a file and a cronjob in it. than try to add this file to cronjob file. can call subprocess to execute a command (sudo)
- [ ] find out if a cronjob also works if I make a log into a file 
- [ ] if task before is yes then just create an folder where everything lands in 
- [ ] if no than always create two jobs. 0ne with log and one with no log
'''
from crontab import CronTab
import subprocess

def writeInCrontab():
    subprocess.run("crontab -l > /Users/maxhager/Projects2022/CronjobManager/temp", shell=True)
    with open("temp", "w") as f:
        f.write("")
    subprocess.run("crontab /Users/maxhager/Projects2022/CronjobManager/temp", shell=True)
    subprocess.run("crontab /Users/maxhager/Projects2022/CronjobManager/Cronjobs.txt", shell=True)
    
        
if __name__ == "__main__":
    #run a python script with subprocess sudo
    #createCronjob()
    writeInCrontab()

