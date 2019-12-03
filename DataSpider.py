import urllib.request
from bs4 import BeautifulSoup
import re

response = urllib.request.urlopen('https://jinrong.swufe.edu.cn/szdw/teachers.htm')
result = response.read().decode('utf-8')
# print(type(result))
soup = BeautifulSoup(result, 'html.parser')
item_group = soup.find('div', id='tealist').find_all('a', class_='a1')

name_list = []  # 存放所有老师的姓名
email_list = []  # 存放所有的教师的email
teacher_url = []  # 存放所有的教师的页面链接
url1 = []  # 暂存信息
url_suffix = []  # 存放所有的教师的页面链接后面不同的部分

professor_num = 0  # 25个
associate_professor = 0  # 29个
lecturer = 0
another = 0

for item in item_group:
    name = item.text.strip()
    name_list.append(name)

for item in item_group:
    url = item['href']
    url1.append(url)

for url in url1:
    url = url[7:]
    url_suffix.append(url)

teacher_url = ['https://jinrong.swufe.edu.cn/info' +
               url for url in url_suffix]  # 得到每个老师页面链接存放在一个list中
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'  # 电子邮件正则表达式
regex = re.compile(pattern, flags=re.IGNORECASE)
for url in teacher_url:
    response1 = urllib.request.urlopen(url)
    htmlText = response1.read().decode('utf-8')

    email = regex.findall(htmlText)
    if len(email) > 0:
        email1 = email[0]
    else:
        email1 = ""
    email_list.append(email1)  # 得到每个老师的邮件，存放在email_list中

    if htmlText.__contains__('副教授'):
        associate_professor += 1
    elif htmlText.__contains__('教授'):
        professor_num += 1
    elif htmlText.__contains__('讲师'):
        lecturer += 1
    else:
        another += 1

teacher_info = list(zip(name_list, email_list))  # 教师信息，包含名字和邮件
print(teacher_info)
print("教授：%d副教授：%d讲师：%d其他：%d"% (professor_num, associate_professor, lecturer, another))
