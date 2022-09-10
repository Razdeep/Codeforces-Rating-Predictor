import logging

logger = logging.getLogger('Scraper')

class Scraper:
    
    def getName(self, soup, handle) -> str:
        try:
            filter_1 = soup.find('div', attrs={'class': 'main-info'})
            filter_2 = filter_1.findAll('div')
            filter_3 = filter_2[1].find('div')
            name = filter_3.text.split(',')[0]
            logger.info('getName() returned:' + name)
            return name
        except Exception as e:
            logger.warn('Error while getting name')
            logger.exception(e)
            return 'Not Found'

    def getCurrentRatings(self, soup, handle) -> str:
        try:
            filter_1 = soup.find('div', attrs={'class': 'info'})
            filter_2 = filter_1.find('ul')
            filter_3 = filter_2.find('li')
            filter_4 = filter_3.find('span')
            current_ratings = filter_4.text
            logger.info('getCurrentRatings() returned:' + current_ratings)
            return current_ratings
        except Exception as e:
            logger.exception(e)
            return 'Not Found'

    def getUniversity(self, soup, handle) -> str:
        filter_1 = soup.find('div', attrs={'class':'main-info'})
        filter_2 = filter_1.findAll('div')
        university = ''
        if len(filter_2) > 3:
            filter_3 = filter_2[3].find('a')
            university = filter_3.text
        logger.info('getUniversity() returned:' + university)
        return university

    def getRank(self, soup, handle) -> str:
        filter_1 = soup.find('div', attrs={'class':'main-info'})
        filter_2 = filter_1.find('div')
        filter_3 = filter_2.find('span')
        rank = filter_3.text
        logger.info('getRank() returned:' + rank)
        return rank

    def getProfileURL(self, soup, handle) -> str:
        filter_1 = soup.find('div', attrs={'class': 'title-photo'})
        filter_2 = filter_1.find('div')
        filter_3 = filter_2.find('div')
        filter_4 = filter_3.find('div')
        filter_5 = filter_4.find('img')
        img_url = filter_5['src'][2:]
        img_url = f'https://{img_url}'
        logger.info(f'getProfileURL() returned: {img_url}')
        return img_url

if __name__ == '__main__':
    from bs4 import BeautifulSoup
    import requests
    handle = 'razdeep'
    url = f'https://codeforces.com/profile/{handle}'
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html5lib')
    scraper = Scraper()
    scraper.getCurrentRatings(soup, handle)