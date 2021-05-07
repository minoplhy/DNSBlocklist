import os
import sys
from re import sub
from shutil import copyfile

infile = sys.argv[1]
outfile = sys.argv[2]

f = open(infile,'r')
a = ['0.0.0.0 ','0.0.0.0']
lst = []
for line in f:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
f.close()
f = open(infile,'w')
for line in lst:
    f.write(line)
f.close()

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
   f.write('\n'.join([line + ' CNAME .\n'])) # add CNAME . if file does not start with ;   
f.close()

remove_words = ['127.0.0.1','255.255.255.255','::1','fe80','ff0']

with open(infile, 'r') as f:
  lines = f.read().splitlines()
with open(infile, 'w') as f:
    for line in lines:
        if not any(remove_word in line for remove_word in remove_words):
            f.write('\n'.join([line + '\n']))

copyfile(infile, outfile) # copy input file to output file
os.remove(infile) # remove input file

exit()