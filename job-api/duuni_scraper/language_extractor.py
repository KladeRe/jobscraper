import requests
from bs4 import BeautifulSoup
from duuni_scraper.error_classes import ConnectionError, ClassnameError
from duuni_app.models import JobListing
from duuni_scraper.languages import programming_language_entries

def extract_languages(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(ConnectionError(url, response.status_code))
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    job_info_class = "gtm-apply-clicks description description--jobentry"
    title_class = "text--break-word"
    def class_has_word(tag):
        return tag.has_attr('class') and any('description--jobentry' in class_ for class_ in tag['class'])
    info = soup.find(class_has_word)
    job_title = soup.find(class_=title_class)

    if not info:
        raise ClassnameError(job_info_class, url)

    posting_entry = JobListing.objects.create(title=job_title.text, url=url)
    for language in programming_language_entries:
        if language.name.lower() in info.text.lower():
            posting_entry.programming_languages.add(language)
            posting_entry.save()

    
        



