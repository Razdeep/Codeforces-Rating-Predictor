from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def predict(handle):
    url = 'https://codeforces.com/contests/with/'
    url += handle
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html5lib')

    table = soup.find('table', attrs = {'class' : 'user-contests-table'})
    # table

    ratings_tr = table.findAll('tr')
    ratings_tr = ratings_tr[1:]
    # ratings_tr

    ratings_list = []
    for this_row in ratings_tr:
        ratings_list.append(int(this_row.findAll('td')[5].text))
            
    ratings_list.reverse()

    # ratings_list




    ratings_df = pd.DataFrame(ratings_list, columns = ['RATINGS'])

    ratings_df.head()


    # In[10]:


    idx_df = pd.DataFrame(np.arange(1, len(ratings_list) + 1, dtype='int64'), columns = ['CONTEST'])

    idx_df.head()


    # In[11]:


    df = pd.concat([idx_df, ratings_df], axis = 1)
    df.columns = ['CONTEST', 'RATINGS']

    df.head()




    model = LinearRegression()
    model.fit(idx_df, ratings_df)


    # In[14]:


    output = model.predict([[ratings_df.shape[0] + 1]])
    output = int(output)
    return output

    # ## Visualization

    # plt.plot(idx_df, ratings_df)
    # plt.title('Username : {}'.format(handle))
    # plt.xlabel('Contest ID')
    # plt.ylabel('Ratings')
    # dummy_dataset = pd.DataFrame(np.arange(0, ratings_df.shape[0]))
    # plt.plot(dummy_dataset, model.predict(dummy_dataset))


if __name__ == '__main__':
    predict('razdeep')


