#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time
# 1. The files and directories to be backed up are specified in a list.
#source = ['/home/swaroop/byte', '/home/swaroop/bin']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that
source = ['C:/Python27/Doc','C:/Python27/Scripts']
# 2. The backup must be stored in a main backup directory
#target_dir = '/mnt/e/backup/' # Remember to change this to what you will be using
target_dir = 'e:/bak/pythontst/'
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "d:\soft_install_path\haozip\HaoZipC.exe a -tzip %s %s -r " % (target,' '.join(source))

# Run the backu p

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED' 

