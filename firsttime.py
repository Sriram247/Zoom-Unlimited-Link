import subprocess
import sys
import time
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
exec(open('get-pip.py').read())
time.sleep(1)
exec(open('install.py').read())


