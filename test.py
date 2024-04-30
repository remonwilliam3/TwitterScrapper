import requests
from bs4 import BeautifulSoup
import time
import random

# Function to scrape a Twitter account for mentions of a stock symbol
def scrape_twitter_account(url, ticker):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://twitter.com/',
    }

    # Add random delay to mimic human behavior
    time.sleep(random.uniform(1, 3))

    # Fetch the Twitter page
    response = requests.get(url, headers=headers)
    
    # Check if the page was fetched successfully
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tweets = soup.find_all('div', class_='tweet')
        
        # Count the mentions of the stock symbol
        mention_count = sum(1 for tweet in tweets if ticker in tweet.text)
        
        return mention_count
    else:
        print("Failed to fetch the Twitter page.")
        return None

# List of Twitter accounts
twitter_accounts = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox"
]

# Stock ticker to look for
ticker = "$TSLA"

# Time interval for scraping session (in minutes)
interval_minutes = 10

# Main function to perform scraping at regular intervals
def main():
    while True:
        print(f"Scraping started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Loop through each Twitter account and scrape
        for account in twitter_accounts:
            mention_count = scrape_twitter_account(account, ticker)
            if mention_count is not None:
                print(f"{ticker} was mentioned {mention_count} times in the last {interval_minutes} minutes on {account}.")
        
        print(f"Scraping completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Waiting for the next scraping session...")
        
        # Wait for the specified interval before scraping again
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    main()
