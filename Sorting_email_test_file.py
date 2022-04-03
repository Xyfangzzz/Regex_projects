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
   
    
        
    
        
   
