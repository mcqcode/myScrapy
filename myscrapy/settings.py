# Scrapy settings for myscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'myscrapy'

SPIDER_MODULES = ['myscrapy.spiders']
NEWSPIDER_MODULE = 'myscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
   'cookies' : '__g=sem; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1602338585; __fid=57a7b23aec7c4e4174861e38e2fcca94; lastCity=100010000; __c=1602338585; __l=r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0s0000aPch_Smgbn9TpI-AGF9S_K9taRqqXkcTNMh1Tt0EHByftmIfwPcOQFWhr6G3kG_un1brl__IxKnYmczULVDDRSNSFEQotvo4xk5vHbCEkcUno5lPwBJrcsOpDs0fWV9_Tv0_Sp1UvU1zroi9HPn5CWjQEa16DAPaW4BObfPRWSM4fkMaBb0oO--TwX9NSn7igmP1qPjRwUEqYzIvHfh6aP.7R_NR2Ar5Od663rj6t8AGSPticrZA1AlaqM766WHGek3hcYlXE_sgn8mE8kstVerQKMks4OgSWS534Oqo4yunOogEOtZV_zyUr1oWC_knmx5u9qVXZutrZ1en5o_seOU9tqvZvSXZxeT5MY3IMVseqvxj4e_rOW9vN3x5ksePSZut5gKDS6k9tqSZuu9LSLj4SrZxvmxU_lqJIZ0lp4W63rjzJspMg8WW4r_nU_DY2yQLfYQS_zUM1F9CnNR2Ar5Od663rj6t8AGSPticcYlm2erp-muCy2qLu_v20.U1Yk0ZDqmhq1TsKspynqn0KY5yFETLn0pyYqnWcd0ATqUvwlnfKdpHdBmy-bIfKspyfqn1c0mv-b5HcLrfKVIjYknjD4g1DsnHIxnW0dnNtknjc1g1nznW9xn1Dzn7t1PW0k0AVG5H00TMfqnWRs0AFG5HDdr7tznjwxnWDL0AdW5HDsnj7xnH6vnW0zPHcsPdtznjRkg17xnH0zg1Dsn-ts0Z7spyfqn0Kkmv-b5H00ThIYmyTqn0K9mWYsg100ugFM5H00TZ0qn0K8IM0qna3snj0snj0sn0KVIZ0qn0KbuAqs5H00ThCqn0KbugmqTAn0uMfqn0KspjYs0Aq15H00mMTqnH00UMfqn0K1XWY0mgPxpywW5gK1QyNWp6KGuAnqHbG2RsKYmgFMugfqPWPxn7t1nj00IZN15HDkP1RYnjfYnHR3PHnLnHc3P1TY0ZF-TgfqnHmsnWn1rjR3nHnvn6K1pyfqmWNbrjN9uAmsnjFBPWnzPfKWTvYqfYDYrHcdfR77fWFAPDR1nsK9m1Yk0ZwdIjYk0ZK85H00TydY5H00Tyd15H00uANYgvPsmHYs0ZGY5H00UyPxuMFEUHYsg1Kxn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1KxPjnknjb4PNtYn1DsrHbdg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00XMK_Ignqn0K9uAu_myTqr0K_uhnqn0KbmvPb5fKYTh7buHYLPW0znjc0mhwGujd7n1wjwb77PWFaPj6zfW64nHRYPWRLwDDzPDRsPH97P0KEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBn3njc4n10zninznW0snanznW0sna3snj0snj0Wninzc10WnH0Wna3snjb4P1bWni3snj0knj00TNqv5H08P1wxna3sn7tsQW0sg108rjwxna3vP7tsQWns0AF1gLKzUvwGujYs0APzm1Ykn10vPs%26ck%3D1673.1.126.313.177.304.172.647%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26us%3D1.0.1.0.1.301.0%26wd%3D%26bc%3D110101&l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3Djava%26city%3D100010000%26industry%3D%26position%3D&g=%2Fwww.zhipin.com%2Fsem%2F10.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-pc-BOSS-JD02-B19KA02084%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3D%25E9%2580%259A%25E7%2594%25A8%26keyword%3Dwww.hugoboss.cn%26bd_vid%3D8202080693516625012%26csource%3Dboctb&friend_source=0&friend_source=0; __a=25369700.1602338585..1602338585.19.1.19.19; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1602341812; __zp_stoken__=8972bYSkYI3c3YjBpXmxgXVZSVQsuBHghdTZ6aB4eVGtFV1lpPDInTQU1KnYQVm5oNmNKDAAXN251Y0IdS3V2RxFadz5AOHwXfE55bghwECF4XzZBWiAICVVdWyESYD0UMDJAHz0%2FOE4FQHJ%2BRQ%3D%3D'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'myscrapy.middlewares.MyscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'myscrapy.middlewares.MyscrapyDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'myscrapy.pipelines.MyscrapyPipeline': 300,
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
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
