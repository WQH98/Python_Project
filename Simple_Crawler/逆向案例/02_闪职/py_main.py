import requests
from lxml import etree
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

session = requests.Session()

login_url = 'http://shanzhi.spbeen.com/login/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

resp = session.get(login_url, headers=headers)
tree = etree.HTML(resp.text)
token = tree.xpath('//form[@id="login_button"]/input/@value')[0]
rsa_key = tree.xpath('//div[@class="col content"]/input/@value')[0]
rsa_key = RSA.importKey('-----BEGIN PUBLIC KEY-----\n' + rsa_key + '\n-----END PUBLIC KEY-----')

password = 'test1234567890'
rsa = PKCS1_v1_5.new(key=rsa_key)
new_password = rsa.encrypt(password.encode('utf-8'))
new_password = base64.b64encode(new_password)

data = {
    'username': 'test1234567890',
    'password': new_password,
    'csrfmiddlewaretoken': token
}

resp = session.post(login_url, headers=headers, data=data)
print(resp.text)
