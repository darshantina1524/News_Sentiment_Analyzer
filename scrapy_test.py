# Run with
#
# scrapy runspider a3-dtina-itunes-topapps-1.py –t csv –o out - > a3-dtina-itunes-topapps1.csv


# A very bare minimum spider


from scrapy.spider import Spider

class ItunesSpider(Spider):
    name = 'google_news_2'
    handle_httpstatus_list = [404,403]
    allowed_domains = ['google.com']
    start_urls = ["https://news.google.com/?hl=en-US&gl=US&ceid=US:en"]
    custom_settings = {'DOWNLOAD_DELAY':0.5}

    def parse(self,response):
            apps = response.xpath('//div/article')
            items = []
            for app in apps:
                item = {}
                item['News'] = app.xpath('./h4/a/text()').extract()
                items.append(item)

            return items
