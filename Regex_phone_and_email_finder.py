import re
import pyperclip
matches = []
sortEmail2 = []
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4})', re.VERBOSE)
text = str(pyperclip.paste())
SearchPhone = phoneRegex.findall(text)
for x in range(len(SearchPhone)):
       print(SearchPhone[x][0])
emailRegex = re.compile(r'((\w+|\d+)(\@)(gmail|outlook|yahoo|student.auhsd|nostarch)(.com|.org|.us))')
SearchEmail = emailRegex.findall(text)
for y in range(len(SearchEmail)):
    print(SearchEmail[y][0])
    sortEmail2.append(SearchEmail[y][0])
#Gmailsearch = re.compile(r'\w+\@gmail')
#sortEmail = Gmailsearch.findall(" ".join(matches))
#print(sortEmail)
print(sortEmail2)
for i in range(len(sortEmail2)):
    temp = sortEmail2[i]
    for j in range(len(sortEmail2)):
        if sortEmail2[j] == 'gmail' and sortEmail2[i] != 'gmail':
            sortEmail2[i] = sortEmail2[j]
            sortEmail2[j] = temp
           

print(list(reversed(sortEmail2)))
    





