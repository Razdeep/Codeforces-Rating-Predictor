from app import app
from flask import render_template, request
from app.scraper import Scraper
from app.predictor import Predictor
from app.visualizer import Visualizer
import requests
import logging
from bs4 import BeautifulSoup

logger = logging.getLogger('Routes')
scraper = Scraper()
predictor = Predictor()
visualizer = Visualizer()

@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'POST'):
        handle = request.form.get('handle')
        logger.info('Handle received from post request: ' + handle)
        try:
            url = f'https://codeforces.com/profile/{handle}'
            logger.info('Profile URL to be fetched: ' + url)
            html_page = requests.get(url)
            logger.info('Codeforces Profile HTML page received through GET')
            soup = BeautifulSoup(html_page.content, 'html5lib')
            logger.info('CF Profile HTML parsed by bs4')
            name = scraper.getName(soup, handle)
            current_ratings = scraper.getCurrentRatings(soup, handle)
            profile_URL = url
            img_url = scraper.getProfileURL(soup, handle)
            predicted = predictor.predict(handle)
            university = scraper.getUniversity(soup, handle)
            rank = scraper.getRank(soup, handle)
            graph_url = visualizer.visualize(handle)

            return render_template('result.html', handle=handle,
                                                    name=name,
                                                    profile_URL=profile_URL,
                                                    current_ratings=current_ratings,
                                                    university=university,
                                                    rank=rank,
                                                    predicted=predicted, 
                                                    img_url=img_url,
                                                    graph_url=graph_url)
        except Exception as e:
            logger.exception(e)
            return render_template('404.html')
      
    return render_template('index.html')