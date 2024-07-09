import subprocess
def check(iv, cr):
    if subprocess.run(['./oracle', change(iv) ,change(cr)]).returncode == 0:
        return True
    return False
def modify(st, p, t):
    st = bytearray(st)
    st[p] = t
    st = bytes(st)
    return st
def get(st, p):
    return bytearray(st)[p]
def change(byte_data):
    return ''.join(f'{byte:02x}' for byte in byte_data).upper()
IV = bytes.fromhex('CA1DB62557DDD1AD98953B7C8EB43F85')
Crypto = bytes.fromhex('8B2B9DCD0A6633A612E415CE64B42CF1')
if check(IV, Crypto):
    print('123')

res = bytes(16)

for i in range(15, -1, -1):
    t = 15 - i + 1
    IV1 = bytes(16)
    for j in range(15, i, -1):
        IV1 = modify(IV1, j, t ^ res[j])
    
    for j in range(0, 256):
        IV1 = modify(IV1, i, j)
        # IV1[i] = j
        if check(IV1, Crypto):
            res = modify(res, i, t ^ j)
            # res[i] = t ^ j
            break
    print(res)
print(res)
# b'\x99.\xd5Wd\xa9\x9c\x9e\xeb\xe6{\x1b\xbd\x95=\x87'
        
