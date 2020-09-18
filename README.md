# github_crawl

Script to crawl through Github by username or repo to mine for .py files in creating NLP datasets.

## Installation

This package can be easily installed by following these steps:

- **Clone the repo:**
```shell
$ git clone https://github.com/lupks/github_crawl
```
 
- **Install any missing dependencies:**
```shell
$ pip install -r requirements.txt
```

## Usage 

### repo_crawl
To mine for .py files by repo, pass the following arguments:
- URL of repo
- Output directory of where you want to save python script as text file

```shell
$ python src/repo_crawl.py {url} {output directory}
```

### user_crawl
To mine for .py files by username, pass the following arguments:
- Github username *(i.e. 'lupks')*
- Output directory of where you want to save python script as text file

```shell
$ python src/repo_crawl.py {username} {output directory}
```

## Contact/Issues
For help or issues involving github_crawl, please submit a GitHub issue.


## License 
MIT
