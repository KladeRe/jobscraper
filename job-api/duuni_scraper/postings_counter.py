import requests
import re
import math
from bs4 import BeautifulSoup
from duuni_scraper.error_classes import ConnectionError, ClassnameError


def count_postings():
    url = "https://duunitori.fi/tyopaikat?haku=developer"

    response = requests.get(url)

    if response.status_code != 200:
        raise ConnectionError(url, response.status_code)


    # Parse html document
    soup = BeautifulSoup(response.text, 'html.parser')

    meta_class_name = "m-b-10-on-all text--body text--left text--center-desk"
    postings_amount_tag = soup.find(class_=meta_class_name)

    if not postings_amount_tag:
        raise ClassnameError(meta_class_name, url)
    
    postings_amount_text = postings_amount_tag.text

    postings_amount_str = re.search(r'\d+', postings_amount_text).group()

    postings_amount = int(postings_amount_str)

    websites = math.ceil(postings_amount / 20)

    return websites
            


