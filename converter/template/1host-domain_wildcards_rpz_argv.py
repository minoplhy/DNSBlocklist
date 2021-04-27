import os
import sys
from re import sub
from shutil import copyfile

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as f:
    file = f.read().split('\n')
for i in range(len(file)):
    file[i] = sub(r'#', ';', file[i])
#print(file)
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
f.close()

with open(infile, 'r') as f: # load file 
 lines = f.read().splitlines() # read lines
with open(infile, 'w') as f: # load file in write mode
 for line in lines:
  if line.startswith(';'):
   f.write('\n'.join([line + '\n']))
  elif not line.strip():
   f.write('\n'.join([line + '\n']))
  elif not line.startswith(';') and line.strip():
   f.write('\n'.join([line + '\n'])) and f.write('\n'.join(['*.'+line+'\n'])) # add *. and CNAME . if file does not start with ;   
f.close()

with open(infile, 'r') as f: # load file 
 lines = f.read().splitlines() # read lines
with open(infile, 'w') as f: # load file in write mode
 for line in lines:
  if line.startswith(';'):
   f.write('\n'.join([line + '\n']))
  elif not line.strip():
   f.write('\n'.join([line + '\n']))
  elif line.startswith('*.') or not line.startswith(';') and line.strip():
   f.write('\n'.join([line + ' CNAME .\n'])) # add CNAME . if line start with *.
f.close()

copyfile(infile, outfile) # copy input file to output file
os.remove(infile) # remove input file

exit()
