import requests

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