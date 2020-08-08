import scrapy

f = open("C:/Users/Cong/PycharmProjects/CrawlBaomoi/tutorial/tutorial/Output/BaoMoi.txt", "a", encoding="utf8")

class BaoMoi(scrapy.Spider):
    name = "BaoMoi"
    start_urls = ["https://baomoi.com/"]

    def parse(self, response):
        articles = response.xpath('//div[@class="story"]')
        for article in articles:
            link = article.css('div.story__meta a.cache::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(link), callback=self.parse2)

        next_page = response.xpath('//div[@class="pagination__controls"]/a[@class="btn btn-sm btn-primary"]/@href').extract_first()
        if next_page and '2' not in next_page :
            yield scrapy.Request(response.urljoin(next_page))
    def parse2(self, response):
        def getbody(query):
            s = ""
            for i in response.css(query):
                p_body = i.get()
                s = s + p_body + '\n'
            return s

        f.write('Title: ' + response.css('div.article h1.article__header::text').extract_first() + '\n')
        f.write('Source: ' +response.css('div.article div.article__meta a.source::text')[-1].extract().strip() + '\n')
        f.write('Description: ' +response.css('div.article div.article__meta time::text').extract_first() +'\n')
        f.write('Content: ' + getbody('div.article__body p.body-text::text') + '\n')