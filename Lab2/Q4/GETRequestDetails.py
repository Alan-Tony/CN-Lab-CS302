import requests
from requests.api import head

url = input('Enter a URL: ')
response = requests.get(url)

print("Status code: ", response.status_code)    #Returns a number that indicates the status (200 is OK, 404 is Not Found)

print("Headers: ")    #Returns a dictionary of response headers
print("********************************")
headers = response.headers
for key, value in headers.items():
    print(f"{key} : {value}")
print("********************************")

print("History: ", response.history)    #Returns a list of response objects holding the history of request (url)
print("Encoding: ", response.encoding)  #Returns the encoding used to decode response.text
print("Reason: ", response.reason)  #Returns a text corresponding to the status code
print("Cookies: ", response.cookies)    #Returns a CookieJar object with the cookies sent back from the server
print("Elapsed: ", response.elapsed)    #Returns a timedelta object with the time elapsed from sending the request to the arrival of the response
print("Request: ", response.request)    #Returns the request object that requested this response