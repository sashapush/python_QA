import requests
from bs4 import BeautifulSoup

url = "https://www.gov.pl/web/poland-businessharbour-en/itspecialist"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
data = requests.get(url, headers=headers)
# print(data.text)
soup = BeautifulSoup(data.content, "html.parser")
# print(soup.prettify())
titles = []
# ass = soup.findAll(class_="ipc-metadata-list-summary-item__li ipc-metadata-list-summary-item__li--link")
# ass = soup.find(class_="ipc-metadata-list-summary-item__li ipc-metadata-list-summary-item__li--link").getText()
# will append all shows
# for a in ass:
#    titles.append(a.getText())
test = soup.find_all("a", href=True)
ass = []
with open("file.txt", "w") as file:
    for t in test:
        # print(type(t)) # <class 'bs4.element.Tag'>
        # if "\b.co\b" in t:
        if ".co" in t["href"]:
            print(t["href"])
            file.write(t["href"].strip() + "\n")
