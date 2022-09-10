from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import logging

logger = logging.getLogger('Predictor')

class Predictor:
    def predict(self, handle) -> int:
        url = f'https://codeforces.com/contests/with/{handle}'
        html_page = requests.get(url)
        soup = BeautifulSoup(html_page.content, 'html5lib')
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
        output = model.predict([[ratings_df.shape[0] + 1]])
        output = int(output)
        logger.info(f'predict() returned: {output}')
        return output  

if __name__ == '__main__':
    predict('razdeep')