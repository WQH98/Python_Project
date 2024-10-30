"""
涉及技术：
    headers中设置User_Agent反爬机制
    通过network抓包 分析ajax的请求和参数
    通过for循环请求不同的参数的数据
    利用pandas实现excel的合并与保存
"""

import requests
import pandas as pd
# 通过包含这个库 可以在编译时不提示warning
import warnings
# warnings.filterwarnings('ignore')

url = "http://tianqi.2345.com/Pc/GetHistory"

headers = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81"""
}


def craw_table(year, month):
    """
    提供年份和月份爬取对应的表格数据
    """
    params = {
        "areaInfo[areaId]": 54511,
        "areaInfo[areaType]": 2,
        "date[year]": year,
        "date[month]": month,
    }

    resp = requests.get(url, headers=headers, params=params)
    data = resp.json()["data"]
    # 可以解析网页中所有的表格 返回一个列表
    # data frame
    df = pd.read_html(data)[0]
    return df


df_list = []
for year in range(2011, 2022):
    for month in range(1, 13):
        print("爬取：", year, month)
        df = craw_table(year, month)
        df_list.append(df)

pd.concat(df_list).to_excel("北京十年天气数据.xlsx", index=False)
