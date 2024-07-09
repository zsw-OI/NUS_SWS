import subprocess
cypher_type = ['-aes-128-ecb', '-aes-128-cbc', '-aes-128-cfb', '-aes-128-ofb']
for tp in cypher_type:

    subprocess.run(['openssl', 'enc', '-e', tp, '-in', 'message.txt', '-out', 'encrypted.bin', '-K', '00112233445566778889aabbccddeeff', '-iv', '0102030405060708'])
    bt = []
    with open('./encrypted.bin', 'rb') as file:
        bt = bytearray(file.read())
    bt[29] = 114
    with open('./corrupted.bin', 'wb') as file:
        file.write(bytes(bt))
    subprocess.run(['openssl', 'enc', '-d', tp, '-in', 'corrupted.bin', '-out', 'decrypted' + tp + '.txt', '-K', '00112233445566778889aabbccddeeff', '-iv', '0102030405060708'])
