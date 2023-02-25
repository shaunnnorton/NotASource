from fetch import get_refrences
from bs4 import BeautifulSoup
from requests import Response

#This file contains functions to process data recieved from other functions or external sources. 
def format_refrences(soup: BeautifulSoup):
    ref = {
        "text":'',
        "links":'',
        "ref_num":0
    }
    reflist = []
    for data in soup:
        ref.links = data.find_all("a")
