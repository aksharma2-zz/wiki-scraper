from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
  try:
    get(url, auth=('user', 'pass'), stream=True) as response:
      if is_good_response(resp):
        return resp.content
      else:
        return None

  except RequestException as re:
    log_error('Error in request {0} : {1}'.format(url, str(e)))
    return None

def is_good_response(resp):
  # Check if resp is HTML
  return (resp.status_code == requests.codes.ok and 'html' in response.headers['content-type'])

simple_get('https://realpython.com/blog/')