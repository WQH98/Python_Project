import uuid
import random
import base64
from Crypto.Cipher import DES3


def des3(data_string):
    BS = 8
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    # DES3的MODE_CBC模式只有前24位有效
    key = b"appapiche168comappapiche168comap"[0: 24]
    iv = b"appapich"

    plaintext = pad(data_string).encode("utf-8")

    # 使用MODE_CBC创建cipher
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    result = cipher.encrypt(plaintext)
    return base64.b64encode(result).decode("utf-8")


def run():
    imei = str(uuid.uuid4())
    nano_time = random.randint(5136066335773, 7136066335773)
    device_id = "397671"
    udid = des3(f"{imei}|{nano_time}|{device_id}")
    print(udid)


if __name__ == "__main__":
    run()
