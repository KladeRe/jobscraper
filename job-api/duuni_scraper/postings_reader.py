import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from duuni_scraper.error_classes import ConnectionError, ClassnameError
from duuni_scraper.language_extractor import extract_languages

base_url= "https://duunitori.fi/tyopaikat?haku=developer&sivu="



def read_websites(website_amount):

    with ThreadPoolExecutor(max_workers=4) as executor:

        for i in range(1, website_amount+1):

            url = base_url + str(i)
            response = requests.get(url)

            if response.status_code != 200:
                raise ConnectionError(url, response.status_code)

            # Parse html document
            soup = BeautifulSoup(response.text, 'html.parser')

            postings_grid_class_name = "grid-sandbox grid-sandbox--tight-bottom grid-sandbox--tight-top"
            postings_class_name = "grid grid--middle job-box job-box--lg"

            postings_grid = soup.find(class_=postings_grid_class_name)

            if not postings_grid:
                raise ClassnameError(postings_class_name, url)
            
            postings = postings_grid.find_all(class_=postings_class_name)


            if not postings:
                raise ClassnameError(postings_class_name, url)
            

            def get_href(posting_tag):
                anchor = posting_tag.find("a")
                href_value = anchor.get("href")
                return href_value

            href_values = map(get_href, postings)
            for href in href_values:
                extract_languages( f"https://duunitori.fi{href}")
