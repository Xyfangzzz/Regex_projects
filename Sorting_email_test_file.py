email = [('Will', 'student'), ('Chris','gmail'), ('Miriam', 'outlook'), ('Mom','gmail')]
sortedEmail = []

for x in range(len(email)):
    sortedEmail.append(email[x][1])

print(email)
print(sortedEmail)

for i in range(len(sortedEmail)):
    temp = sortedEmail[i]
    for j in range(len(sortedEmail)):
        if sortedEmail[j] == 'gmail' and sortedEmail[i] != 'gmail':
            sortedEmail[i] = sortedEmail[j]
            sortedEmail[j] = temp

print(list(reversed(sortedEmail)))
<<<<<<< HEAD
   
    
=======

########################Seperate code. #####################################################################################   
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
        print(i, j)
        if sortEmail2[j] == 'gmail' and sortEmail2[i] != 'gmail':
            sortEmail2[i] = sortEmail2[j]
            sortEmail2[j] = temp
            if sortEmail2[j] == 'outlook' and sortEmail2[i] != 'gmail' or 'outlook':
                    sortEmail2[i] = sortEmail2[j]
                    sortEmail2[j] = temp

print(list(reversed(sortEmail2)))
    



>>>>>>> test
        
    
        
   
