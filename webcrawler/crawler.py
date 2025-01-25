import requests
from bs4 import BeautifulSoup
from collections import deque
import time
import yake

from .config import ALLOWED_DOMAIN

def is_valid_url(url):
    if url.startswith("http") and ALLOWED_DOMAIN in url:
        return True
    return False

def extract_keywords_links(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    links = []
    for a_tag in soup.find_all("a", href=True):
        link = a_tag["href"]
        if link.startswith("/"):
            link = f"https://{ALLOWED_DOMAIN}{link}"
        links.append(link)

    text = soup.get_text(separator=" ")
    kw_extractor = yake.KeywordExtractor(
        lan="en", n=1, dedupLim=0.9, top=100
    )
    keywords = [kw[0] for kw in kw_extractor.extract_keywords(text)]

    return links, keywords

def bfs_crawl(seed_url, max_urls=1003, mongo_collection=None):
    visited = set()
    queue = deque([seed_url])

    num_crawled = 0
    start_time = time.time()
    cum_extracted_urls = 0
    cum_crawlable_urls = 0
    cum_extracted_keywords = 0
    time_stamps = []
    extracted_urls = []
    crawlable_urls = []
    extracted_keywords = []

    while queue and num_crawled < max_urls:
        current_url = queue.popleft()
        if current_url in visited:
            continue

        visited.add(current_url)
        print(f"\ncrawling [{num_crawled + 1}/{max_urls}]: {current_url}")
        try:
            response = requests.get(current_url, timeout=5)
            if response.status_code == 200:
                html_content = response.text
                # extract links and keywords
                all_links, keywords = extract_keywords_links(html_content)
                # store keywords in mongodb
                if mongo_collection is not None:
                    from .mongo_utils import store_in_mongo
                    doc_body = {
                        "url": current_url,
                        "keywords": keywords,
                        "timestamp": time.time()
                    }
                    store_in_mongo(mongo_collection, doc_body)
                # updating bfs
                num_crawled += 1
                extracted_count = len(all_links)
                crawlable_count = 0
                for link in all_links:
                    if is_valid_url(link) and link not in visited:
                        crawlable_count += 1
                        queue.append(link)

                keyword_count = len(keywords)
                cum_extracted_urls += extracted_count
                cum_crawlable_urls += crawlable_count
                cum_extracted_keywords += keyword_count
                time_stamps.append(time.time() - start_time)
                extracted_urls.append(cum_extracted_urls)
                crawlable_urls.append(cum_crawlable_urls)
                extracted_keywords.append(cum_extracted_keywords)
            else:
                print(f"skipping {current_url} due to status code {response.status_code}")
        except Exception as e:
            print(f"error crawling {current_url}: {e}")
            continue

    return (time_stamps, extracted_urls, crawlable_urls, extracted_keywords)
