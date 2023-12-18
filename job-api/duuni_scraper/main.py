from duuni_scraper.postings_counter import count_postings
from duuni_scraper.postings_reader import read_websites

def webscrape():
    # This is needed to get all job postings
    
    websites_amount = count_postings()

    read_websites(websites_amount)


    


