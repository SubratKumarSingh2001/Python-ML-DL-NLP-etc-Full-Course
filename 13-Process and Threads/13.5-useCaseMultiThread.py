''''
Real-World Example: Multithreading for I/O-Bound Tasks
Scenario: Web Scrapping
Web Scrapping: It often involves making numerous network requests to fetch web pages. These tasks are I/O Bound because they spent lot of time waiting for response from the servers.
Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently 

https://docs.langchain.com/oss/python/langchain/overview
https://docs.langchain.com/oss/python/langchain/models
https://docs.langchain.com/oss/python/langchain/tools
'''

import threading
import requests
#beautiful soup used in web scrapping that parse the raw HTML/XML documents making it easy to navigate to different parts of the webpage, it represent in tree like structure 
from bs4 import BeautifulSoup

#we will web scrap these urls
urls = ["https://docs.langchain.com/oss/python/langchain/overview", "https://docs.langchain.com/oss/python/langchain/models", "https://docs.langchain.com/oss/python/langchain/tools"]

def fetch_contents(url) :
    response = requests.get(url) #server send the html response to the request made
    soup = BeautifulSoup(response.content, 'html.parser') #response.content is the raw html content and html.parser tells BeautifulSoup which parser to use to convert raw HTML into a tree-like structure so that we can easily access elements using objects.
    print(f"Fetched {len(soup.text)} characters from {url}")

#now we create the list of threads
threads =[]

for url in urls :
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

#This for loop to ensure the main thread is paused till all the worker threads work complete then only rest part of program will be executed
for thread in threads :
    thread.join()
 
print("All web pages fetched")