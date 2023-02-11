import requests

# to send cookies we need to use dictionary:
cookie = {"visit-month": "June"}

r = requests.get("https://rahulshettyacademy.com/", cookies=cookie)
print(r.status_code)

s = requests.session()
s.cookies.update({"test-cookie": "Tasty"})
# https://httpbin.org/#/Cookies/get_cookies
c = s.get("https://httpbin.org/cookies",
          cookies={"request cookie": "yummy"})  # cookies are combined with session cookies
print(c.json())

print(c.text)
