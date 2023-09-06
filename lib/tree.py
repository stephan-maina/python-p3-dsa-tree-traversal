from bs4 import BeautifulSoup

def get_element_by_id(html_content, target_id):
    soup = BeautifulSoup(html_content, 'html.parser')
    element = soup.find(id=target_id)
    return element
