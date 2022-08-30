import scrapy
import os


class OrdiSpider(scrapy.Spider):
    name = "ordi_spider"

    # Change json encoding for $ in output
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    # URL where from spiders gets information
    url = "https://ordi.eu/sulearvutid?___store=en&___from_store=et"
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
            }

    def start_requests(self):
        # Set the headers here.
        yield scrapy.http.Request(self.url, headers=self.headers)

    def parse(self, response):
        """
        We’ll use CSS selectors for now since CSS is the easier option and a
        perfect fit for finding all the items on the page.
        If you look at the HTML for the page, you'll see that each item is specified with the
        class item.
        Since we're looking for a class, we'd use .item for our CSS selector.
        All we have to do is pass that selector into the response object
        """
        ordi_selector = '.item'
        for ordi_computer in response.css(ordi_selector):
            """
            The item object we’re looping over has its own css method, 
            so we can pass in a selector to locate child elements
            """
            title_selector = 'h2 ::text'
            price_selector = './/*[contains(@class,"price-box")]//*/text()'
            img_selector = 'img ::attr(src)'
            yield {
                'Title': ordi_computer.css(title_selector).extract_first(),
                'Price': ordi_computer.xpath(price_selector).extract_first(),
                'Picture href': ordi_computer.css(img_selector).extract_first(),
            }

        # define a selector for the "next page" link
        next_page = '.next ::attr(href)'

        # extract the first match, and check if it exist0s
        next_page = response.css(next_page).extract_first()

        if next_page:
            page_url = response.urljoin(next_page)
            yield scrapy.Request(page_url, self.parse,  headers=self.headers)


if __name__ == "__main__":
    os.system("scrapy runspider -O ordi_scrape_spider_output.json ordi_scrape_spider.py")
