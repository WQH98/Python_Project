import re

# re.l	是匹配对大小写不敏感
# re.M	多行匹配 影响到^和$
# re.S	使.匹配包括换行符在内的所有字符

str = """
    <a href="http://www.baidu.com">百度</a>
    <A href="http://www.ali.com">阿里</A>
    <a href="http://www.Tencent.com">腾讯</a>
    <a href="http://www.baidu.com">百度
    双引号</a>
    <a href='http://www.baidu.com'>百度
    单引号</a>
"""

# 匹配所有的正常的a链接 小写a
print(re.findall('<a href="(.*?)">(.*?)</a>', str))
# 修正符号
# 不匹配大小写
print(re.findall('<a href="(.*?)">(.*?)</a>', str, re.I))
# 匹配大小写 多行匹配 可以匹配换行符
print(re.findall('<a href="(.*?)">(.*?)</a>', str, re.I|re.M|re.S))
# 匹配大小写 多行匹配 可以匹配换行符 加匹配单引号
print(re.findall('<a href=[\'"](.*?)[\'"]>(.*?)</a>', str, re.I|re.M|re.S))