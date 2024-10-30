# 美剧网址

# url = 'https://www.99meijutt.com/play/103594-0-0.html'

# 抓取思路
# 1、先看当前网址是什么类型的视频网站
# 2、查看当前网站的视频 是怎样加载的（一次性加载的还是分了多个视频段进行加载的）
# 3、如果是多个片段的文件 需要找到当前包含多个片段文件的地址
"""
m3u8
https://c3.monidai.com/20240403/inPARg5l/index.m3u8
#EXTM3U
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=998000,RESOLUTION=1280x720
https://c3.monidai.com/ppvod/D05907B9F85611B0C13676C5D41193A2.m3u8
https://c3.monidai.com/ppvod/D05907B9F85611B0C13676C5D41193A2.m3u8
"""


