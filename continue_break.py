list = ['Milk','Butter','Curd','Bread','Rice']
for x in list:
    if x == 'Rice':
        continue
    print(x)

for x in list:
    if x == 'Rice':
        print(x,' is not available')
        break
