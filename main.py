import requests, json
from urllib.parse import unquote
from bs4 import BeautifulSoup

urls = "123 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".lower().split(" ")
array = []
def get_series(filename):
  for i in range(len(urls)):
    urls[i] = "https://hitomi.la/all" + filename + "-" + urls[i] + ".html"
  for url in urls:
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    serieses = soup.select("body > div > div.content > ul > li > a")
    for series in serieses:
      array.append((unquote(series.get("href")[1:-9]), series.contents[0]))

  with open(filename+'.json', 'w', encoding='utf-8') as file:
    json.dump(array, file, indent='\t')
  return True

list(map(get_series, ["artists", "characters", "series", "tags"]))
