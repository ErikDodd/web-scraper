import requests
import urllib.request
import time
from bs4 import BeautifulSoup


# Create function named get_citations_needed_count
# takes in a url string and returns an integer.
def get_citations_needed_count(url):
    soup = BeautifulSoup(response.text, "html.parser")
    get_citation = soup.findAll('p')
    citation_count = 0
    for citation in get_citation:
        if "citation needed" in citation.getText():
            citation_count += 1
    return citation_count


#Create function named get_citations_needed_report
#takes in a url string and returns a report string
#the string should be formatted with each citation listed in the order found.
def get_citations_needed_report(url):
    soup = BeautifulSoup(response.text, "html.parser")
    get_citation = soup.findAll("p")
    results = []
    for citation in get_citation:
        if "citation needed" in citation.getText():
            results.append(citation.text)
    print(results)





if __name__ =='__main__':
    url = "https://en.wikipedia.org/wiki/History_of_Mexico"
    response = requests.get(url)
    #results = parse(response.text)
    #print(results)
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))