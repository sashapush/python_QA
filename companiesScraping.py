import requests
from bs4 import BeautifulSoup

url = "https://www.gov.pl/web/poland-businessharbour-en/itspecialist"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}
data = requests.get(url, headers=headers)
# print(data.text)
soup = BeautifulSoup(data.content, "html.parser")
titles = []
test = soup.find_all("a", href=True)  # we look for all a tags with href attribute
ass = []
with open("emails.txt", "w", encoding="utf-8") as file:
    for t in test:
        # print(type(t)) # <class 'bs4.element.Tag'>
        # if "\b.co\b" in t:
        if "mailto:" in t["href"]:
            print(t["href"])
            file.write(t["href"].strip() + "\n")
file.close()

with open("websites.txt", "w", encoding="utf-8") as file:
    for t in test:
        # print(type(t)) # <class 'bs4.element.Tag'>
        # if "\b.co\b" in t:
        if "https://" in t["href"]:  # if any(s in line for s in ('string1', 'string2', ...)):
            print(t["href"])
            file.write(t["href"].strip() + "\n")
file.close()
