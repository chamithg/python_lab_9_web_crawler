# Course: CIS 117 PythonProgramming
# Name:   Chamith Gamage
# Description:  Programming with Namespaces, Exception Control Flow
# Application:  Data Analysis and Handling Input Errors
# Development Environment:  macOSX 12.4
# Version:  Python 3.10.4
# Date:  10/11/22


# Program Source Statements

from urllib.request import urlopen 
import datetime
import re


# variable to hold the url
url = "http://www.nasonline.org"

#  list of topics
topics =["research",  "climate","evolution", "cultural",
        "leadership","medicine"]

# create the date object of datetime module.
date = datetime.datetime.now()

# empty string to hold decoded website as a string
content=""

#try decode the website, exept returns an error message
try:
    response = urlopen(url) 
    html = response.read() 
    content += html.decode().lower()
except:
    print("Error: Decoding website failed! check the url")

# validates if the content holds a string befor continue.
# if content is empty which means parsing website was not successed.
# do nothing if content is empty.

if content !="":
    
    # this regex patern will find all type of html tags.
    html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"

    
    # all matches in the content string will be removed.
    # the text in between html tags will be spared.
    string_without_tags= re.sub(html_pattern, '', content)

    # print out date in YYYY-MM-DD format
    print("Today's date is "+date.strftime("%Y")+"-"+date.strftime("%m")
        +"-"+date.strftime("%d"))
    
    # iterate over list of topics and find the frequent of each in the 
    # string without tags string.
    for topic in topics: 
        
        # keeps the count of each topic
        n = string_without_tags.count(topic) 
        
        # print out the count of each topic
        print('{} appears {} times.'.format(topic,n)) 
        

'''
### output 1(failed)

chamithgamage@Chamiths-Air lab9 % /usr/local/bin/python3 "/Users/chamithgamage/
Desktop/CSM- FALL-2022/Python/lab9/chamithLab9.py"
Error: Decoding website failed! check the url


### output 1(success)

chamithgamage@Chamiths-Air lab9 % /usr/local/bin/python3 "/Users/chamithgamage/
Desktop/CSM- FALL-2022/Python/lab9/chamithLab9.py"

Today's date is 2022-11-08
research appears 9 times.
climate appears 1 times.
evolution appears 1 times.
cultural appears 3 times.
leadership appears 2 times.
medicine appears 7 times.


'''