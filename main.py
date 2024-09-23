import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
from unidecode import unidecode
import linecache

url = "http://desk.outsourcing-gate.com/ent/shaderalsamak"
login = {'pin': '4339'}
link = "http://desk.outsourcing-gate.com/customers/shaderalsamak"
with requests.Session() as session:
    post = session.post("http://desk.outsourcing-gate.com/ent/shaderalsamak", data=login)

data = []
names = []
nums = []
adr = []
date = []
links = []
page_num = 1
while True:
    try:
        r = session.get(link)
        src = r.content
        soup = BeautifulSoup(src, "lxml")
        page_limit = 10472
        if (page_num > page_limit // 10):
            print("pages ended, exit")
            break

        name = soup.find_all("a", {"target": "_blank"})
        data = soup.find_all("a")
        num = soup.find_all("td")

        for links in data:
            link = "http://desk.outsourcing-gate.com" + (links.get('href'))
        print(link)
        i = 0
        while i < 55:
            names.append(str(num[i].text))

            nums.append(unidecode(num[i + 1].text))
            adr.append(num[i + 2].text)
            date.append(str(num[i + 5].text))
            i += 6

        page_num += 1
        print("page switched")
    except:
        print("error")

file_list = [names, nums, adr, date]
exported = zip_longest(*file_list)
with open("E:\Book1.csv", "w", encoding="UTF-8") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Name", "Phone", " Address", "Registered"])
    wr.writerows(exported)
