# TODO: Add the ability to cycle through every directory looking for .py files
import requests
from bs4 import BeautifulSoup
import re


def repo_crawl(input_url, output_dir):
    base_url = input_url
    page = requests.get(base_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    """
    Crawl through directories looking for .py files
    """

    print('Crawling Github for .py files...')
    for span in soup.find_all('a', class_="js-navigation-open link-gray-dark"):
        if '.py' in span.text:
            url = base_url + '/blob/master/' + span.text

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
                dir_link = span.text
                span_url = base_url + '/tree/master/' + dir_link
                page = requests.get(span_url)
                soup = BeautifulSoup(page.content, 'html.parser')

                for span in soup.find_all('a', class_="js-navigation-open link-gray-dark"):
                    if '.py' in span.text:
                        py_url = base_url + '/blob/master/' + dir_link + '/' + span.text
                        print(py_url)
                        page = requests.get(py_url)
                        soup = BeautifulSoup(page.content, 'html.parser')

                        corpus = ''
                        for td in soup.find_all('td'):
                            corpus = corpus + td.text + '\n'

                        corpus = corpus.replace('\n\n', '\n')

                        with open(output_dir, 'a+') as f:
                            f.write(corpus)
            except:
                pass
    print('Done!')


if __name__ == "__main__":
    repo_crawl(sys.argv[0], sys.argv[1])
