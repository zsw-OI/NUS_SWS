IV = bytes.fromhex('CA1DB62557DDD1AD98953B7C8EB43F85')
Crypto = bytes.fromhex('8B2B9DCD0A6633A612E415CE64B42CF1')
ans = b'\x99.\xd5Wd\xa9\x9c\x9e\xeb\xe6{\x1b\xbd\x95=\x87'
IV = bytearray(IV)
ans = bytearray(ans)
for i in range(len(IV)):
    ans[i] ^= IV[i]
print(bytes(ans))