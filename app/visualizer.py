from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os
import secrets
import logging

logger = logging.Logger(__name__)

def visualize(handle):
    try:
        url = f'https://codeforces.com/contests/with/{handle}'
        html_page = requests.get(url)
        soup = BeautifulSoup(html_page.content, 'html5lib')
        logger.info("Successfully parsed soup")
        table = soup.find('table', attrs = {'class' : 'user-contests-table'})
        ratings_tr = table.findAll('tr')
        ratings_tr = ratings_tr[1:]
        ratings_list = []
        for this_row in ratings_tr:
            ratings_list.append(int(this_row.findAll('td')[5].text))
        ratings_list.reverse()
        ratings_df = pd.DataFrame(ratings_list, columns = ['RATINGS'])
        ratings_df.head()
        idx_df = pd.DataFrame(np.arange(1, len(ratings_list) + 1, dtype='int64'), columns = ['CONTEST'])
        idx_df.head()
        df = pd.concat([idx_df, ratings_df], axis = 1)
        df.columns = ['CONTEST', 'RATINGS']
        df.head()
        model = LinearRegression()
        model.fit(idx_df, ratings_df)

        # Visualization

        plt.plot(idx_df, ratings_df)
        plt.title(f'Username : {handle}')
        plt.xlabel('Contest ID')
        plt.ylabel('Ratings')
        dummy_dataset = pd.DataFrame(np.arange(0, ratings_df.shape[0]))
        plt.plot(dummy_dataset, model.predict(dummy_dataset))
        output_filename = secrets.token_hex(16) + '.png'
        path = os.path.abspath('.') + '/app/static/generated/'
        os.makedirs(path, exist_ok = True)
        plt.savefig(path + output_filename)
        plt.close()
        logger.info('visualize() returned: ' + output_filename)
        return output_filename
    except Exception as e:
        msg = 'Couldn\'t generate graph'
        logger.warning(msg)
        raise Exception(e)



if __name__ == '__main__':
    visualize('razdeep')


