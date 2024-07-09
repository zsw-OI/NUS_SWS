import subprocess
import string
with open('DOTA2024Lab2Password.encoded', 'r') as file:
    encoded = list(file.readline())
for i in encoded:
    print(i)
res = ''
alpha_list = list(string.ascii_letters) + [str(i) for i in range(0, 10)]
for i in range(len(encoded)):
    print(i)
    for t in alpha_list:
        tg = True
        print(t)
        res1 = res + t
        with open("try.in", "w") as file:
            file.write(res1)
        print("!!!")
        # process = subprocess.Popen(['./wse', '<', 'try.in', '>', 'try.out'])
        # process.wait(timeout=0.5)  
        subprocess.run(['./wse', '<', 'try.in', '>', 'try.out'])
        print("!!!!")
        with open('try.out', "r") as file:
            ans = list(file.readline())
        for i in range(len(ans)):
            if ans[i] != encoded[i]:
                tg = False
        if tg == True:
            res = res1
            break
print(res)
            