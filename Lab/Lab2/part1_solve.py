import string
mp = dict()
with open('testdata.out','r') as file:
    for i in list(string.ascii_lowercase):
        line = file.readline()
        mp[i] = list(line)
    for i in list(string.ascii_uppercase):
        line = file.readline()
        mp[i] = list(line)
    for i in range(0, 10):
        line = file.readline()
        mp[str(i)] = list(line)
for a in mp:
    print(a + str(':'), end='')
    for i in mp[a]:
        print(i, end = ' ')
    print()
with open('dict.out', 'w') as file:
    for a in mp:
        file.write(a + str(':'))
        for i in mp[a]:
            file.write(i + ' ')
        file.write('\n')
    