# CS 6675 Web Crawler

This web crawler is a Python-based implementation that uses a **BFS** approach and extracts keywords from crawled pages using the **YAKE** (Yet Another Keyword Extractor) library and stores relevant metadata in a MongoDB database.

---
## Installation

### Prerequisites
1. **Python**: Ensure Python 3.x is installed.
2. **MongoDB**: Install MongoDB on your device to store crawled data.
4. **Python Libraries**:
   Install required Python libraries:
   ```bash
   pip install requests beautifulsoup4 yake pymongo
   ```
Resulting plots can be viewed in the /plots directory  

### Run the Crawler
Run this line to start the crawling process:
```bash
python3 -m webcrawler.main
```
The MongoDB server should be started on port 27017.
