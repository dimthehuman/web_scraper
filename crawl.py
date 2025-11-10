from urllib.parse import urlparse, urljoin
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

def get_urls_from_html(html, url):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    return [urljoin(url, link.get("href")) for link in links if link.get("href")]

def get_images_from_html(html, url):
    soup = BeautifulSoup(html, "html.parser")
    images = soup.find_all("img")
    return [urljoin(url, image.get("src")) for image in images if image.get("src")]

def extract_page_data(html, page_url):
    return {
        "url": page_url,
        "h1": get_h1_from_html(html),
        "first_paragraph": get_first_paragraph_from_html(html),
        "outgoing_links": get_urls_from_html(html, page_url),
        "image_urls": get_images_from_html(html, page_url),
    }