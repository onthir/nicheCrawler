from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


base_url = 'https://www.niche.com/colleges/'



def crawl_website(link, univ, sity):
    response = urlopen(link)
    context = response.read()

    new = univ.replace("-", " ")
    # souped
    soup = bs(context, 'lxml')

    # find the data
    data = soup.findAll(attrs={'class': 'scalar__value'})
    actual2 = (data[2].get_text())

    # appedn to a file
    with open(str(univ) + "/cost.txt", 'a') as file:
        file.writelines( str(actual2) + " --> " + sity+ "\n")
        print(str(new) + " added to the file")


def cost_crawlwer(university_path):
    with open(str(university_path) + "/formatted.txt", 'r') as file:
        f = file.readlines()
        for r in f:
            nr = str(r).replace("\n", "")
            nt = nr.replace("-", " ")
            url = base_url + str(r).replace("\n", "") + "/cost/"
            print("Starting Crawling " + str(r))
            try:
                crawl_website(url, university_path, nt)
            except:
                print("Error")