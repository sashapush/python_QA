import requests

# to send cookies we need to use dictionary:
cookie = {"visit-month": "June"}

r = requests.get("http://rahulshettyacademy.com/",  # allow_redirects=False,
                 cookies=cookie, timeout=50)
# allow_redirects=False will not allow redirects, stops after first status code
# timeout is used in case endpoint has high load and repsonds after a set amount of time

# REDIRECTS history
# as it turned out there is a redirect before hiting this url #302-200
print(r.history)  # will return 301
print(type(r.history))
# assert [<Response [301]>] in r.history
print(r.status_code)

s = requests.session()
s.cookies.update({"test-cookie": "Tasty"})
# https://httpbin.org/#/Cookies/get_cookies
c = s.get("https://httpbin.org/cookies",
          cookies={"request cookie": "yummy"})  # cookies are combined with session cookies
print(c.json())
print(c.text)

# Attachments in request
url = 'https://petstore.swagger.io/v2/pet/123/uploadImage'
files = {'file': open('C:\\Users\\Alex\\Pictures\\[DaddySubs] Shingeki no Kyojin - S04E20 (79)[v0][1080p x264 10bits]['
                      'Multi-Subtitles].mkv_snapshot_07.18.555.jpg', 'rb')}
req = requests.post(url, files=files)
print(req.status_code)
print(req.text)
