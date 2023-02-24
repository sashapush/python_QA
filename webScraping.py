import requests
from bs4 import BeautifulSoup

genre = "comedy"
url = f"https://www.imdb.com/find/?q={genre}&s=tt&ttype=ep&exact=true&ref_=fn_tt_ex"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
data = requests.get(url, headers=headers)
# print(data.text)
soup = BeautifulSoup(data.content, "html.parser")
# print(soup.prettify())
titles = []
ass = soup.findAll(class_="ipc-metadata-list-summary-item__li ipc-metadata-list-summary-item__li--link")
# ass = soup.find(class_="ipc-metadata-list-summary-item__li ipc-metadata-list-summary-item__li--link").getText()
# will append all shows
# for a in ass:
#    titles.append(a.getText())


# will append only UNIQUE shows
for a in ass:
    if a.getText() in titles:
        continue
    else:
        titles.append(a.getText())

# titles.append(soup.find("section", {"class": "findList"}).getText())

print(titles)

# Next task - check that genre = comedy
baseUrl = "https://www.imdb.com"
for a in ass:
    subUrl = a["href"]
    print(subUrl)
    subData = requests.get(baseUrl + subUrl, headers=headers)
    borsch = BeautifulSoup(subData.content, "html.parser")
    g = borsch.findAll("div",
                       class_="ipc-metadata-list ipc-metadata-list--dividers-all sc-fba22acc-1 biEmms ipc-metadata-list--base")
    print(g)
