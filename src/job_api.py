from apify_client import ApifyClient
import os
from dotenv import load_dotenv

load_dotenv()

APIFY_API_TOKEN = os.getenv('APIFY_API_TOKEN')

apify_client = ApifyClient(APIFY_API_TOKEN)

def fetch_linkedin_jobs(search_query, location='Australia', rows = 40):
    run_input = {
            "title": search_query,
            "location": location,
            "rows": rows,
            "proxy": {
                "useApifyProxy": True,
                "apifyProxyGroups": ["RESIDENTIAL"],
            }
        }
    run = apify_client.actor("BHzefUZlZRKWxkTck").call(run_input=run_input)
    jobs = list(apify_client.dataset(run["defaultDatasetId"]).iterate_items())
    return jobs