import requests
from bs4 import BeautifulSoup
import re

import .repo_crawl

def user_crawl(username, output_dir):
  search_url =f'https://github.com/{username}?q=&type=&language=python'

  page = requests.get(search_url)
  soup = BeautifulSoup(page.content, 'html.parser')

  """
  Crawl User's .py files by search link
  """

  for a in soup.find_all('a', class_="d-inline-block"):
      try:
        user_url = f'https://github.com/{username}/' + a.text.strip()
        print(user_url)

        repo_crawl(user_url, output_dir)
      
      except:
        pass

if __name__ == "__main__":
    user_crawl(sys.argv[1], sys.argv[2])


