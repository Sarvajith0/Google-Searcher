import requests
import sys
import bs4
import webbrowser

res = requests.get('https://google.com/search?q'+''.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
link_elements = soup.select('.r a')
link_to_open = min(5, len(link_elements))
for i in range(linkToOpen):
    webbrowser.open('https://google.com' + link_elements[i].get('href'))
