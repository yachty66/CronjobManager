import subprocess
import config
subprocess.call(['git', 'add', '-A'])
subprocess.call(['git', 'commit', '-m', '{}'.format("Update")])
subprocess.call(['git', 'push', 'https://{}@github.com/yachty66/CronjobManager.git'.format(config.gitToken)])