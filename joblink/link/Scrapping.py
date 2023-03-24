import requests
from bs4 import  BeautifulSoup

class Scrapper:
    def __init__(self,url):
        self.url = url

    def get_html(self):
        response = requests.get(self.url)
        print(response.status_code)
        print("++++Scrapping in Progress")
        soup = BeautifulSoup(response.text,"html.parser")
        print("++Returning Html")
        return soup

    def process_html(self):
        All_urls =[]
        job_title_list =[]
        postedDate_list = []
        soup = self.get_html()
        rawData = soup.find_all('tr',{'class':'data-row'})
        if len(rawData) > 0:
            for ele in rawData:
                if ele is not None:
                    aTag = ele.find('a')
                    if aTag is not None:
                        link = aTag.get('href')
                        link = "https://jobs.ltts.com/" + link
                        job_title = aTag.text.strip()
                        postedDate = ele.find('span',{'class':'jobDate visible-phone'})
                        if postedDate is not None:
                            postedDate_list.append(postedDate.text.strip())
                        if link not in All_urls:
                            All_urls.append(link)
                            job_title_list.append(job_title)

            my_dict = {"JobTitle":job_title_list,
                            "Link_to_job":All_urls,
                               "PostedDate":postedDate_list }
            return my_dict

url = "https://jobs.ltts.com/go/AMERICA/4637210/"
obj = Scrapper(url)
data = obj.process_html()
