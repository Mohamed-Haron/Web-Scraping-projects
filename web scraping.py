from bs4 import BeautifulSoup

with open('home.html','r') as html_content:
    content = html_content.read()
    
    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.find_all('div', class_ = 'card')
    for course in courses_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

    