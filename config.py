import os

SEED_URL = "https://cc.gatech.edu/"
MAX_URLS = 1003
ALLOWED_DOMAIN = "cc.gatech.edu"

# directories
PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

# mongo configs
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "crawler_db"
COLLECTION_NAME = "pages"
