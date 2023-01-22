from bs4 import BeautifulSoup
import lxml
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=javascript&txtLocation=').text
soup=BeautifulSoup(html_text,'lxml')

def findingJobs():
    js_jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    res_arr=[]
    for job in js_jobs:
        cmpny_name= job.find('h3',class_='joblist-comp-name').text.strip()
        skills=job.find('span',class_='srp-skills').text.strip().split(',')
        exp= job.find('ul',class_='top-jd-dtl clearfix').li.contents[1]
        obj={
            "companyName":cmpny_name,
            "skills":skills,
            "exp":exp
        }
        res_arr.append(obj)

    print(res_arr)

if __name__=='__main__':
    findingJobs()


