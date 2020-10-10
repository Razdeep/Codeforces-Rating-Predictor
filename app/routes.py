from app import app
from flask import render_template, request
from app import scrapers
from app import predictor
from app import visualizer
import requests
import logging
from bs4 import BeautifulSoup
import logging

@app.route('/', methods=['GET', 'POST'])
def home():
    logger = logging.Logger(__name__)
    if (request.method == 'POST'):
        handle = request.form.get('handle')
        # soup = 0
        try:
            url = f'https://codeforces.com/profile/{handle}'
            html_page = requests.get(url)
            logger.info('Codeforces Profile HTML page received through GET')
            soup = BeautifulSoup(html_page.content, 'html5lib')
            logger.info('CF Profile HTML parsed by bs4')
            name = scrapers.getName(soup, handle)
            current_ratings = scrapers.getCurrentRatings(soup, handle)
            profile_URL = url
            img_url = scrapers.getProfileURL(soup, handle)
            predicted = predictor.predict(handle)
            university = scrapers.getUniversity(soup, handle)
            rank = scrapers.getRank(soup, handle)
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
            logging.exception(str(e))
            return render_template('404.html')
      
    return render_template('index.html')