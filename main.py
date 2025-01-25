from .config import (
    SEED_URL, MAX_URLS, MONGO_URI, DB_NAME, COLLECTION_NAME
)
from .mongo_utils import get_mongo_collection
from .crawler import bfs_crawl
from .plotter import plot_crawl_stats

def main():
    collection = get_mongo_collection(uri=MONGO_URI, db_name=DB_NAME, collection_name=COLLECTION_NAME)
    (times, extracted_urls, crawlable_urls, extracted_keywords) = bfs_crawl(seed_url=SEED_URL, max_urls=MAX_URLS, mongo_collection=collection)
    plot_crawl_stats(times, extracted_urls, crawlable_urls, extracted_keywords)
    print("\nCrawler finished!")

if __name__ == "__main__":
    main()
