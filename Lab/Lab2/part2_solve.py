import subprocess
cipher_type = ['aes-128-cbc', 'aes-128-cfb']
with open('Lab2-2.bin', 'rb') as file:
    st = bytes(file.read())
for i in range(0, 128):
    st1 = st
    for j in range(0, i):
        st1 = st1 + b'\x00'
    print(len(st1))
    with open('testdata.bin', 'wb') as file:
        file.write(st)
    subprocess.run(['openssl', 'enc', '-d', '-aes128', '-in', 'testdata.bin', '-out', 'res.out', '-K', '00112233445566778889aabbccddeeff', '-iv', '0102030405060708'])