import os
from re import sub
from shutil import copyfile

infile = "adg.txt"
outfile = "adg.rpz"

f = open(infile,'r')
a = ['||','^']
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
    file[i] = sub(r'!', ';', file[i])
#print(file)
with open(infile, 'w') as f1:
    f1.writelines(["%s\n" % item  for item in file])
	

# thanks someone on StackOverFlow

with open(infile, 'r') as f: # load file 
 lines = f.read().splitlines() # read lines
with open(infile, 'w') as f: # load file in write mode
   f.write('\n'.join([line + '  CNAME .' for line in lines if not line.startswith(';')])) # add CNAME . if file does not start with ;
      
copyfile(infile, outfile)
os.remove(infile)
# end
