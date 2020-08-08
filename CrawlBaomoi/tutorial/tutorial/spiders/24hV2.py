import scrapy

f = open("C:/Users/Cong/PycharmProjects/CrawlBaomoi/tutorial/tutorial/Output/24hV2.txt", "a", encoding="utf8")

class TwentyFourHSpider(scrapy.Spider):
    name = '24hV2'
    allowed_domains = ['24h.com.vn']
    start_urls = ['https://www.24h.com.vn']
    def parse(self, response):
        if response.status == 200 and response.css('meta[property="og:type"]::attr("content")').get() == 'article':

            content = '\n'.join([
                ''.join(c.css('*::text').getall())
                for c in response.css('article.nwsHt.nwsUpgrade p')
            ])
            keywords = response.css('meta[name="keywords"]::attr("content")').get()
            f.write('//////////' + '\n')
            f.write('link: ' + response.url + '\n')
            f.write('title:' + response.css('title::text').get() + '\n')
            f.write('description: ' + response.css('meta[name="description"]::attr("content")').get() + '\n')
            f.write('content: ' + content + '\n')
            f.write('category: ' + response.css('a.sbevt.clrGr.fs12::attr("title")').get() + '\n')
            f.write('pub_date: ' + response.css('div.updTm.updTmD.mrT5::text').get() + '\n')
            f.write('keywords: ' + keywords + '\n')
            f.write('author: ' + response.css('div.nguontin.nguontinD.bld.mrT10.mrB10.fr::text').extract_first() + '\n')

        yield from response.follow_all(css='a[href^="https://www.24h.com.vn"]::attr(href)', callback=self.parse)



