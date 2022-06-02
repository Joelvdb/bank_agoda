import course_number
import requests
from bs4 import BeautifulSoup
import json


def get_url_from_number(number):
    return 'https://bank.aguda.org.il/course/' + str(number)


def get_dict_of_course(number):
    list_of_tests = []
    # Parsing the HTML
    with open("courses/" + str(number)) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    # Finding by id all files
    s = soup.find('div', id='filtered_files').find('ul').findAll('li')
    for line in s:
        list_of_tests.append((line.find('div', attrs={'class': 'content'}).text,
                              'https://bank.aguda.org.il/' + line.find('a', href=True)['href']))
        # print(line.find('div', attrs={'class': 'content'}).text)
        # print('https://bank.aguda.org.il/' + line.find('a', href=True)['href'])
    return list_of_tests


def get_dict_of_all_courses():
    dict = {}
    for i in course_number.get_cs_courses():
        dict.update({i: get_dict_of_course(i)})

    # create json object from dictionary
    json_file = json.dumps(dict)

    # open file for writing, "w"
    f = open("dict.json", "w")

    # write json object to file
    f.write(json_file)

    # close file
    f.close()


get_dict_of_all_courses()
