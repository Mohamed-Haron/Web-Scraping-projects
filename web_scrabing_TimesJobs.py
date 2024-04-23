from bs4 import BeautifulSoup
import requests
import time

print('Enter uninterested skills separated by comma !')
uninterested_skills = input('>>').strip(',')

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(html_text.text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    print(f'filitering out {uninterested_skills}')
    for index,job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text

        if '1 day ago' in published_date:
            company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            skill_list = skills.strip().split(',')
            more_info = job.header.h2.a['href'] 
            #if uninterested_skills not in skills:
            if not any(skill in uninterested_skills for skill in skill_list):
                    with open(f'Job_posts/{index}.txt','w') as f:
                        f.write(f'company name: {company_name.strip()} \n')
                        f.write(f'skills: {skill_list} \n')
                        f.write(f'more info: {more_info}')
                    print(f'file saved {index}')   


          
    

if __name__ == "__main__":
     while True:
        find_job()
        wait_time = 10
        print(f'Please wait {wait_time} minute to update program')
        time.sleep(wait_time * 60)