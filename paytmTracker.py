# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 16:23:40 2019

@author: User
"""
while True:
    import requests
    from bs4 import BeautifulSoup
    page_url="https://paytm.com/movies/mumbai"
    page1_url="https://paytm.com/movies/upcoming-movies"
    browser_agent={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}
    movie_page=requests.get(page_url,headers=browser_agent)
    soup=BeautifulSoup(movie_page.content,"html.parser")
    movie=soup.find_all("div",id="popular-movies")[0].find_all("div",class_="_3Sve")
    popmov=[]
    upcmov=[]
    mov=[]
    for i in movie:
        popmov.append(i.text)
    movie1_page=requests.get(page1_url,headers=browser_agent)
    soup1=BeautifulSoup(movie1_page.content,"html.parser")
    movie2=soup1.find_all("div",class_="_3W-I")[0].find_all("div",class_="_1q0f")
    for i in movie2:
        upcmov.append(i.text.lower())
    for i in upcmov:
        if i in popmov:
            print(i)
            
            
    




