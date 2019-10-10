import glob
import os
#import ipdb


files = glob.glob('step8*')
for pfile in files:
    new_name = '.'.join(pfile.split('.')[2:])
    os.system('cp {pfile} {new_name}'.format(**locals()))
