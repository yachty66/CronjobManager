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
'''from asyncio import subprocess
from crontab import CronTab
def createCronjob():
    #open crontab file with sudo permisson and append a line
    cron = CronTab(user=True)
    job = cron.new(command='echo hello_world')
    job.minute.every(1)
    cron.write()

def writeInCrontab():
    #copy and paste file content from Cronjobs.txt to crontab file
    with open('Cronjobs.txt', 'r') as f:
        with open('/usr/bin/crontab', 'w') as f2:
            for line in f:
                f2.write(line)
    
        
if __name__ == "__main__":
    #run a python script with subprocess sudo
    #createCronjob()
    writeInCrontab()'''
    
with open('/usr/bin/crontab', 'w') as f2:
    f2.write("Hello World")
    

