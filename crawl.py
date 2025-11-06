from urllib.parse import urlparse
from bs4 import BeautifulSoup


def normalize_url(url):
    parsed_url = urlparse(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

def get_h1_from_html(html):    
    soup = BeautifulSoup(html, "html.parser")
    h1_tag = soup.find("h1")
    return h1_tag.get_text(strip=True) if h1_tag else ""

def get_first_paragraph_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    main_section = soup.find("main")
    if main_section:
        first_p = main_section.find("p")
    else:
        first_p = soup.find("p")

    return first_p.get_text(strip=True) if first_p else ""