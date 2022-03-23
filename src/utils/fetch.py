import requests

def test_link(link) -> bool:
    fail_conditions = {

    }
    response = requests.get(link, allow_redirects=True)
    if response.status_code != 200:
        return False, response.status_code
    elif 'Wikipedia' not in response.text or "reflist" not in response.text:
        return False, response.status_code
    
    return True, response.status_code

def get_page(link) -> str:
    return str()