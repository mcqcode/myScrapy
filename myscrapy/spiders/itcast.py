import scrapy
from myscrapy.items import MyscrapyItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['https://www.zhipin.com/']
    start_urls = ['https://www.zhipin.com/job_detail/?query=java&city=100010000&industry=&position=']

    def parse(self, response):
        x = response.xpath("//div[@class='job-title']//a[1]").extract_first()
        print(x)


