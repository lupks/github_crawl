# TODO: Add the ability to cycle through every directory looking for .py files

import requests
from bs4 import BeautifulSoup
import re

base_url = 'https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python'
page = requests.get(base_url)
soup = BeautifulSoup(page.content, 'html.parser')

"""
Crawl through directories looking for .py files
"""

def repo_crawl(output_dir = ''):
  print('Crawling Github for .py files...')
  for span in soup.find_all('a', class_="js-navigation-open link-gray-dark"):

      if '.py' in span.text:
          url = base_url + '/' + span.text

          page = requests.get(url)
          soup = BeautifulSoup(page.content, 'html.parser')

          corpus = ''
          for td in soup.find_all('td'):
              corpus = corpus + td.text + '\n'

          corpus = corpus.replace('\n\n', '\n')

          with open(output_dir, 'a+') as f:
              f.write(corpus)

      else:
          try:
              span_url = base_url + '/' + span.text
              page = requests.get(span_url)
              soup = BeautifulSoup(page.content, 'html.parser')

              for span in soup.find_all('a', class_="js-navigation-open link-gray-dark"):
                  print(span.text)

                  if '.py' in span.text:
                      url = base_url + '/' + span.text

                      page = requests.get(url)
                      soup = BeautifulSoup(page.content, 'html.parser')

                      corpus = ''
                      for td in soup.find_all('td'):
                          corpus = corpus + td.text + '\n'

                      corpus = corpus.replace('\n\n', '\n')

                      with open(output_dir,'a+') as f:
                          f.write(corpus)
          except:
              pass
              
  print('Done!')
  
