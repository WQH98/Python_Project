from Crypto.PublicKey import RSA


rsa_key = RSA.generate(1024)

# 单独导出加密的密钥(public key 公钥)
pub_key = rsa_key.public_key().export_key()
with open("./01_密钥/pub_key.pem", mode='w', encoding='utf-8') as f:
    f.write(pub_key.decode())


# 单独导出解密的密钥(private key 私钥)
pri_key = rsa_key.export_key()
with open("./01_密钥/pri_key.pem", mode='w', encoding='utf-8') as f:
    f.write(pri_key.decode())

