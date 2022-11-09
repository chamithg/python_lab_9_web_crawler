# Course: CIS 117 PythonProgramming
# Name:   Chamith Gamage
# Description:  Programming with Namespaces, Exception Control Flow
# Application:  Data Analysis and Handling Input Errors
# Development Environment:  macOSX 12.4
# Version:  Python 3.10.4
# Date:  10/11/22


# Program Source Statements


import urllib.request
import urllib.parse
import re
import ssl
context = ssl._create_unverified_context()


url = "http://www.nasonline.org/"
valus = {"s":"basics","submit":"search" }
data = urllib.parse.urlencode(valus)
data = data.encode("utf-8")
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req,context=context)
respData = resp.read()

htmlRegexG = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"

paragraphs = re.findall(r'/<(?:"[^"]*"['"]*|'[^']*'['"]*|[^'">])+>/g',str(respData))

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

word_list = str(respData).split()

print(respData)


# for eachP in paragraphs:
#     print(eachP)