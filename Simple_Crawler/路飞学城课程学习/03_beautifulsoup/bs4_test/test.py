from bs4 import BeautifulSoup

with open("./test.html", encoding='utf-8') as fin:
    html_doc = fin.read()

soup = BeautifulSoup(html_doc, "html.parser")

div_node = soup.find("div", id="content")

links = soup.find_all("a")
for link in links:
    print(link.name, link["href"], link.get_text())

img = soup.find("img")
print(img["src"])
