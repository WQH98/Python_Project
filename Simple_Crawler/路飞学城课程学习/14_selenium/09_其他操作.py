from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options


opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')

web = Edge(options=opt)
web.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx')
print(web.page_source)

