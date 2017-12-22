import requests
from bs4 import BeautifulSoup
import urllib
import time

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"
article_chain = [start_url]

def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain

        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        print(article_chain[-1])
        # delay for about two seconds
        time.sleep(2)  # Slow things down so as to not hammer Wikipedia's servers

def continue_crawl(search_history, target_url):
    if  (search_history[-1] == target_url) | (len(search_history) > 25) | (target_url in search_history) | (len(search_history) !=len(set(search_history))):
        return False
    else:
        return True

def find_first_link(url):
    # get the HTML from "url", use the requests library
    # feed the HTML into Beautiful Soup
    first_link = None
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    # find the first link in the article
    # find the first link in that html

    #first_link = soup.find(id="mw-content-text").p.a.get('href')
    #first_link = soup.find(id='mw-content-text').find(class_="mw-parser-output").p.a.get('href')

    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        # It's important to only look at direct children, because other types
        # of link, e.g. footnotes and pronunciation, could come before the
        # first link to an article. Those other link types aren't direct
        # children though, they're in divs of various classes.
        #if element.a:
        if element.find("a", recursive=False):
            #first_link = element.a.get('href')
            first_link = element.find("a", recursive=False).get('href')
            break

    # return the first link as a string, or return None if there is no link

    if first_link:
        first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_link)
        return first_link
    else:
        return None


