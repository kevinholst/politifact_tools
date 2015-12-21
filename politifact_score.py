from __future__ import division, print_function
from bs4 import BeautifulSoup
import requests
import numpy as np

BASE = 'http://www.politifact.com/personalities/'
SCORING = np.array([2, 1, 0, -1, -2, -3])


def get_truthiness_score(name):
    page = requests.get(BASE + name)
    soup = BeautifulSoup(page.content)
    
    values = np.zeros(6, dtype='int')
    
    rulings = soup.find_all('span', {'class': 'chartlist__count'})
    
    for i, ruling in enumerate(rulings):
        values[i] = int(ruling.contents[0].split()[0])
    
    number_of_rulings = values.sum()
    
    values *= SCORING
    score = values.sum()/number_of_rulings
    
    return score
