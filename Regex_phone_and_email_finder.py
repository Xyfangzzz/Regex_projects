import re
import pyperclip
matches = []

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4})', re.VERBOSE)
text = str(pyperclip.paste())
SearchPhone = phoneRegex.findall(text)
for x in range(len(SearchPhone)):
       print(SearchPhone[x][0])
emailRegex = re.compile(r'((\w+|\d+)(\@)(gmail|outlook|yahoo|student.auhsd|nostarch)(.com|.org|.us))')
SearchEmail = emailRegex.findall(text)
for y in range(len(SearchEmail)):
    print(SearchEmail[y][0])





