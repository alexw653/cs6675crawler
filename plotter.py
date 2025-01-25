import matplotlib.pyplot as plt
import os

from .config import PLOTS_DIR

def plot_crawl_stats(time_stamps, extracted_urls, crawlable_urls, extracted_keywords):

    plt.figure(figsize=(8, 5))
    plt.plot(time_stamps, extracted_urls, color="blue", label="Extracted URLs")
    plt.xlabel("Time (s)")
    plt.ylabel("Extracted URLs")
    plt.title("Extracted URLs Over Time")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "extracted_urls.png"))
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(time_stamps, crawlable_urls, color="purple", label="Crawlable URLs")
    plt.xlabel("Time (s)")
    plt.ylabel("Crawlable URLs")
    plt.title("Crawlable URLs Over Time")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "crawlable_urls.png"))
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(time_stamps, extracted_keywords, color="red", label="Extracted Keywords")
    plt.xlabel("Time (s)")
    plt.ylabel("Extracted Keywords")
    plt.title("Extracted Keywords Over Time")
    plt.grid(True)
    plt.legend()
    plt.savefig(os.path.join(PLOTS_DIR, "extracted_keywords.png"))
    plt.show()
