import json
import scrapy
from datetime import datetime

OUTPUT_FILENAME = 'C:/Users/Cong/PycharmProjects/CrawlBaomoi/tutorial/tutorial/Output/24h.txt'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))

class TwentyFourHSpider(scrapy.Spider):
    name = '24h'
    allowed_domains = ['24h.com.vn']
    start_urls = ['https://www.24h.com.vn']

    def parse(self, response):
        if response.status == 200 and response.css('meta[property="og:type"]::attr("content")').get() == 'article':
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
                'keywords': [
                    k.strip() for k in response.css('meta[name="keywords"]::attr("content")').get().split(',')
                ],
                'author': response.css('div.nguontin.nguontinD.bld.mrT10.mrB10.fr::text').extract_first(),
            }

            with open(OUTPUT_FILENAME, 'a', encoding='utf8') as f:
                f.write(json.dumps(data, ensure_ascii=False))
                f.write('\n')
                self.CRAWLED_COUNT += 1
                self.crawler.stats.set_value('CRAWLED_COUNT', self.CRAWLED_COUNT)
                print('SUCCESS:', response.url)

        yield from response.follow_all(css='a[href^="https://www.24h.com.vn"]::attr(href)', callback=self.parse)



