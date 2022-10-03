'''
Notes:
    - it unpractically trying to manage crontab with python because If it is more effiecient to write directly something into a file 
    - I could create a text file which i could use to create a cronjob. always if i update the file i run a py script which will write its content into cronjob
- [x] create python file which adds a line with a string to a txt file when executed 
- [x] try to create a cronjob with python which executes this file every minute
- [ ] create a file and a cronjob in it. than try to add this file to cronjob file. can call subprocess to execute a command (sudo)
- [ ] find out if a cronjob also works if I make a log into a file 
- [ ] if task before is yes then just create an folder where everything lands in 
- [ ] if no than always create two jobs. 0ne with log and one with no log
'''
#from asyncio import subprocess
from crontab import CronTab
import subprocess
#def createCronjob():
    #open crontab file with sudo permisson and append a line
    #cron = CronTab(user=True)
    #job = cron.new(command='echo hello_worlddkdkdkd')
    #job.minute.every(1)
    #c#ron.write()

def writeInCrontab():
    cron = CronTab(user=True)
    cron.remove_all()
    job = cron.new(command='1 echo hello_world')
    cron.write()
    #reading every line from Cronjobs.txt and add line to crontab    
    #with open("Cronjobs.txt", "r") as f:
     ##   for line in f:
        #    job = cron.new(command='1 echo hello_world')
       #     cron.write()
'''import subprocess    
cmd_line = "echo Hello!"
p = subprocess.Popen(cmd_line, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
out = p.communicate()[0]
print out'''

def test():
    #load temp file with running crontab -l > /Users/maxhager/Projects2022/CronjobManager/temp from python file
    subprocess.run("crontab -l > /Users/maxhager/Projects2022/CronjobManager/temp", shell=True)
    #open temp file and empty temp file
    with open("temp", "w") as f:
        f.write("")
    #write in temp file back to cronjob
    subprocess.run("crontab /Users/maxhager/Projects2022/CronjobManager/temp", shell=True)
    #add Cronjobs.txt to cronjob
    subprocess.run("crontab /Users/maxhager/Projects2022/CronjobManager/Cronjobs.txt", shell=True)

        


    
    
    
        
if __name__ == "__main__":
    #run a python script with subprocess sudo
    #createCronjob()
    #writeInCrontab()
    test()

