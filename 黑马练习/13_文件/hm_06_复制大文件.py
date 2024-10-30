# 打开文件
file_read = open("README")
file_write = open("README[复件]", "w")

# 读写操作
while True:
    # 读取一行内容
    text = file_read.readline()
    if not text:
    # if len(text) == 0:
        break
    file_write.write(text)

# 关闭文件
file_read.close()
file_write.close()
