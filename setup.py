import os
import platform

'''
Placeholder for now. Will create a Python 3.5 virtualenv, read requirements.txt, pip install requirements.
Eventually will build executable.
'''

project_name = 'horn_fieldmap'

# Create virtual environment for the project
os.system('virtualenv -p python3 {}'.format(project_name))

# Activate the virtual environment
operating_system = platform.system()
print('Operating system is: {}'.format(operating_system))
if operating_system is 'Windows':
    os.system('call activate {}'.format(project_name))
elif operating_system is 'Linux':
    os.system('source tutorial-env/bin/activate')
    
# Run pip on requirements.txt to install needed Python modules
os.system('pip install -r requirements.txt')