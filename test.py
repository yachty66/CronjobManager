import subprocess
import config
subprocess.call(['git', 'add', '/Users/maxhager/Projects2022/CronjobManager/test.log' '/Users/maxhager/Projects2022/CronjobManager/README.md'], cwd="/Users/maxhager/Projects2022/CronjobManager")
subprocess.call(['git', 'commit', '-m', '{}'.format("Update")])
subprocess.call(['git', 'push', 'https://{}@github.com/yachty66/CronjobManager.git'.format(config.gitToken)])