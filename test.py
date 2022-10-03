import subprocess
import config
subprocess.call(['git', 'add','.'], cwd="/Users/maxhager/Projects2022/CronjobManager")
subprocess.call(['git', 'commit', '-m', 'hallo'], cwd="/Users/maxhager/Projects2022/CronjobManager")
subprocess.call(['git', 'push', 'https://{}@github.com/yachty66/CronjobManager.git'.format(config.gitToken)], cwd="/Users/maxhager/Projects2022/CronjobManager")