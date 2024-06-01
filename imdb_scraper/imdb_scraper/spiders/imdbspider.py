import scrapy

class IMDBSpider(scrapy.Spider):
    name = 'imdbspider'
    start_urls = ['https://m.imdb.com/chart/top/']
    # Define allowed domain
    allowed_domains = ['imdb.com']
    # Define user agent
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    def parse(self, response):
        # Extract title, year, and rating from each li tag
        for movie_li in response.css('ul.ipc-metadata-list li'):
            title = movie_li.css('h3.ipc-title__text::text').get().strip()
            year = movie_li.css('span.cli-title-metadata-item:nth-of-type(1)::text').get().strip()
            rating = movie_li.css('span.cli-title-metadata-item:nth-of-type(3)::text').get().strip()

            yield {
                'title': title,
                'year': year,
                'rating': rating
            }
