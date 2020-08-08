import json
import scrapy
from datetime import datetime

OUTPUT_FILENAME = 'C:/Users/Cong/PycharmProjects/CrawlBaomoi/tutorial/tutorial/Output/test.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))

class VnexpressSpider(scrapy.Spider):
    name = 'vnexpress'
    start_urls = ['https://www.24h.com.vn/tin-tuc-trong-ngay/cong-bo-34-ca-mac-covid-19-moi-trong-do-ha-noi-co-mot-ca-c46a1172084.html']

    def parse(self, response):
        print('Crawling from:', response.url)
        data = {
            'link': response.url,
            'title': response.css('title::text').get(),
            'description': response.css('meta[name="description"]::attr("content")').get(),
            'content': '\n'.join([
                ''.join(c.css('*::text').getall())
                    for c in response.css('article.nwsHt.nwsUpgrade p')
            ]),
            'category': response.css('a.sbevt.clrGr.fs12::attr("title")').get(),
            'pub_date': response.css('div.updTm.updTmD.mrT5::text').get(),
            'keywords': response.css('meta[name="keywords"]::attr("content")').get(),
            'author': response.css('div.nguontin.nguontinD.bld.mrT10.mrB10.fr::text').extract_first(),
        }

        with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
            f.write(json.dumps(data, ensure_ascii=False))
            f.write('\n')
            print('SUCCESS:', response.url)
