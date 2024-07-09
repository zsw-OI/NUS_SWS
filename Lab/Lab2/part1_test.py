import string
import subprocess
with open('testdata.in', 'w') as file:
    for c in list(string.ascii_lowercase):
        for _ in range(0, 3) :
            file.write(c)
        file.write('\n')
    for c in list(string.ascii_uppercase): 
        for _ in range(0, 3) :
            file.write(c)
        file.write('\n')
    for c in range(0, 10) :
        for _ in range(0, 3) : 
           file.write(str(c))
        file.write('\n')
subprocess.run(['./wse', '<', 'testdata.in'])

