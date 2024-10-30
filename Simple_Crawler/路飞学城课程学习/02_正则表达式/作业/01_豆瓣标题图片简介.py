import re
import csv

# 获取图片的url
def get_img(douban_str):
    img_urls = re.findall('<img class="subject-cover" align="left" src="https://img\\d.doubanio.com/view/subject/s/public/s\\d{8}.jpg"/>', douban_str)
    urls = []
    for img_url in img_urls:
        img = re.search("\\bhttps?://\\S+jpg", img_url).group()
        urls.append(img)
    return urls


# 获取标题
def get_title(douban_str):
    img_titles = re.findall('<a class="fleft" href="https://book.douban.com/subject/\\w+/">(.*?)</a>', douban_str)
    return img_titles


# 获取简介
def get_brief_introduction(douban_str):
    img_brief_introduction = re.findall('<p class="subject-abstract color-gray">\\s+(.*?)\\s+</p>', douban_str)
    return img_brief_introduction


if __name__ == "__main__":
    f = open("../素材/豆瓣新书速递.html", "rb")
    douban_strs = f.read().decode("utf-8")
    f.close()
    img_urls_data = get_img(douban_strs)
    img_titles_data = get_title(douban_strs)
    brief_introduction_data = get_brief_introduction(douban_strs)
    datas = []
    for img_url_data, img_title_data, brief_data in zip(img_urls_data, img_titles_data, brief_introduction_data):
        data = [img_title_data, brief_data, img_url_data]
        datas.append(data)

    with open("./豆瓣图书信息.scv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["标题", "简介", "封面"])
        writer.writerows(datas)

