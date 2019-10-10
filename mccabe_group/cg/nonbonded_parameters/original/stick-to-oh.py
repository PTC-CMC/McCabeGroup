import glob
import os

for oldname in [('stick1', 'oh1'), ('stick2', 'oh2')]:
    for oldfile in glob.glob('*{0}*'.format(oldname[0])):
        print(oldfile, oldfile.replace(oldname[0], oldname[1]))
        os.system('cp {0} {1}'.format(oldfile, oldfile.replace(oldname[0], oldname[1])))
