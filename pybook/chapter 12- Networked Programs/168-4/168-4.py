import ssl
import urllib.error
import urllib.request

from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

paragraphs = soup('p')
paragraphs_count = 0
for paragraph in paragraphs:
    paragraphs_count += 1
print(paragraphs_count)
