import string
import requests
from bs4 import BeautifulSoup

def test_link(link: str) -> tuple[bool,int]:
    """Tests that the provided link returns status code 200 and that the response includes 
    'Wikipedia' and 'reflist'."""
    response = get_page(link)
    if response.status_code != 200:
        return False, response.status_code
    elif 'Wikipedia' not in response.text or "reflist" not in response.text:
        return False, response.status_code
    
    return True, response.status_code

def get_page(link: str) -> str:
    """Gets the wikipedia page of the provided link."""
    response = requests.get(link, allow_redirects=True)
    return response

def strip_page(response: str) -> BeautifulSoup:
    soup = BeautifulSoup(response, "html.parser")
    soup.link.decompose()
    soup.meta.decompose()
    soup.script.decompose()
    soup.style.decompose()
    for data in soup(['style', 'script', "meta", "link"]):
        # Remove tags
        data.decompose()
  

    return soup

def get_refrences(soup: BeautifulSoup) -> str:
    sources = []
    referrences = soup.find("ol",class_="references")
    for item in referrences:
        if item.text != "\n":
            sources.append(item.text)
    #print(sources)
    return sources, referrences
