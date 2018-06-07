from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import os
from formatter import *
from costfinder import *

user = input("Enter a state Name: ")
user2 = str(user).lower()
user3 = user2.replace(" ", "-")
l = 1
# directory to store 
directory = str(user).lower() + "/"
# final directory to store universities
final_dir = directory + "cost.txt"

# get page number to take in the range for crawling
url = 'https://www.niche.com/colleges/search/best-colleges/s/' + str(user3)
response = urlopen(url)
context = response.read()

soup = bs(context, 'lxml')
# find page numbers
try:
    page_no = soup.find(attrs={'class':'pagination__pages__selector'})
    raw = (page_no.get_text())
    fresh = raw.replace("Page", "")
    final = fresh.replace(" ", "")
    range_right = int(final[len(final)-1])
except:
    range_right = 1

for i in range(range_right):
    url = 'https://www.niche.com/colleges/search/best-colleges/s/' + str(user3) + '/?page=' + str(i+1)
    response = urlopen(url)
    context = response.read()

    soup = bs(context, 'lxml')
    # get all results
    data = soup.findAll(attrs={'class': 'search-result__title'})
    for d in data:
        z = str(d.get_text())
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + str(user3) + '-universities.txt', 'a') as file:
            file.writelines(z + "\n")
            print(str(l) +" " + str(z))
            l += 1

# # then format the file
# do_it(user)

# # then find the cost
# # 1. 
# cost_crawlwer(user2)