# Scrapy settings for online_school project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "online_school"

SPIDER_MODULES = ["online_school.spiders"]
NEWSPIDER_MODULE = "online_school.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
LOG_LEVEL = "WARNING"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en",
    'Cookie': 'pc_780749445_exam=fangchan; wxLoginUrl=https%3A%2F%2Fks.wangxiao.cn%2Fexampoint%2Flist%3Fsign%3Djz1; autoLogin=true; userInfo=%7B%22userName%22%3A%22pc_780749445%22%2C%22token%22%3A%22083408be-d461-4eaf-80ef-067c12e09f65%22%2C%22headImg%22%3A%22https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FMHR714WET3vlCe9fCNlQAeUqC17uiaRI1UZ81z7g8uhDyZ3u2KXRabXxUsDC0ueIfZo8ZBicEq3mXBqJfqpicJI8nYrH74ltQKqdic7Duv45asI%2F132%22%2C%22nickName%22%3A%22%E7%8E%8B%E6%9C%89%E8%B4%A2%22%2C%22sign%22%3A%22fangchan%22%2C%22isBindingMobile%22%3A%221%22%2C%22isSubPa%22%3A%220%22%2C%22userNameCookies%22%3A%228WruAoRSm2emt%2F38yJSn3w%3D%3D%22%2C%22passwordCookies%22%3A%22du8AQ%2FJkFXN8Z42g8CBbMw%3D%3D%22%7D; token=083408be-d461-4eaf-80ef-067c12e09f65; UserCookieName=pc_780749445; OldUsername2=8WruAoRSm2emt%2F38yJSn3w%3D%3D; OldUsername=8WruAoRSm2emt%2F38yJSn3w%3D%3D; OldPassword=du8AQ%2FJkFXN8Z42g8CBbMw%3D%3D; UserCookieName_=pc_780749445; OldUsername2_=8WruAoRSm2emt%2F38yJSn3w%3D%3D; OldUsername_=8WruAoRSm2emt%2F38yJSn3w%3D%3D; OldPassword_=du8AQ%2FJkFXN8Z42g8CBbMw%3D%3D'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "online_school.middlewares.OnlineSchoolSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "online_school.middlewares.OnlineSchoolDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "online_school.pipelines.OnlineSchoolPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
