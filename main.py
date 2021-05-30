# -*- coding: UTF-8 -*-
import urllib.request as req
import urllib.request
import bs4
import ssl
def uber():
    url2 ="https://www.ubereats.com/tw/taipei/food-delivery/%E8%90%8A%E7%88%BE%E5%AF%8C4158%E5%8C%97%E5%B8%82%E6%96%B0%E6%98%8E%E5%BA%97/8PqQgLcHTCiRI1YkRHCuCg"
    url3 = "https://www.ubereats.com/tw/taipei/food-delivery/%E5%A4%A7%E6%BD%A4%E7%99%BC-%E5%85%A7%E6%B9%96%E4%BA%8C%E5%BA%97-rt-mart/rJyvKJoATqWTNspdU7aynw"
    url = "https://www.ubereats.com/tw/taipei/food-delivery/%E5%A4%A7%E6%BD%A4%E7%99%BC-%E5%85%A7%E6%B9%96%E4%BA%8C%E5%BA%97-rt-mart/rJyvKJoATqWTNspdU7aynw?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMk5vLiUyMDIxJTJDJTIwTGFuZSUyMDE5NiUyQyUyMFhpYW5neWFuZyUyMFJvYWQlMjIlMkMlMjJyZWZlcmVuY2UlMjIlM0ElMjJDaElKQzBDMlZtT3JRalFSUHZZWEpYSzZqNWclMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMjUuMDU2ODM0NyUyQyUyMmxvbmdpdHVkZSUyMiUzQTEyMS41OTQzNDglN0Q%3D"


    re = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    })


    ssl._create_default_https_context = ssl._create_unverified_context
    response = urllib.request.urlopen(url)
    with req.urlopen(re) as res:
        data=res.read().decode("utf-8")

    root=bs4.BeautifulSoup(data, "html.parser")
    data = root.find("div",class_= "f2 f3 cd dx")
    m1 = "close"
    m2 = "open"
    if data == None:
        return m2
    else:
        return m1