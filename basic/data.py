marks = {
        'Ravi': [67,87,78,56,87,90],
        'Rashmi': [89,98,78,56,87,45],
        'Lokesh': [78,75,68,84,95,93]
        }

tot = {}

for stud in marks:
    tot[stud] = sum(marks[stud])
    
lis = list(tot.values())
print('Topper is :', [key for (key, value) in tot.items() if value == max(lis)][0], '\n')
sub = [[],[],[],[],[],[]]
for i in range(6):
    for stud in marks:
        sub[i].append(marks[stud][i])
        
for i in range(6):
    print('Topper in subject', i+1, ' : ', [key for (key, value) in marks.items() if value[i] == max(sub[i])])
    
print('\n Lowest marks scorer is ', [key for (key, value) in tot.items() if value == min(lis)][0], '\n')