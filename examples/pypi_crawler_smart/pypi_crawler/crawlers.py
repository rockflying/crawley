from crawley.scrapers import BaseScraper
from crawley.extractors import XPathExtractor
from models import *
from crawley.crawlers.smart import SmartCrawler

class PackagesAuthorsScraper(BaseScraper):

    #The pages that have the precious data
    matching_urls = ["%"]

    def scrape(self, response):

        project = response.html.xpath("/html/body/div[5]/div/div/div[3]/h1")[0].text
        author = response.html.xpath("/html/body/div[5]/div/div/div[3]/ul/li/span")[0].text

        PackagesAuthors(project=project, author=author)


class PackagesAuthorsCrawler(SmartCrawler):

    #add your starting urls here
    start_urls = ["http://pypi.python.org/pypi"]

    #add your scraper classes here
    scrapers = [PackagesAuthorsScraper]

    #specify you maximum crawling depth level
    max_depth = 1

    #select your favourite HTML parsing tool
    extractor = XPathExtractor

    #an example of a page that you want to scrap
    template_url = "http://pypi.python.org/pypi/Shake/0.5.10"
