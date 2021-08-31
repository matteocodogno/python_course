myfile = open('./resources/fruits.txt')
content = myfile.read()
myfile.close()
print(content)

with open('./resources/fruits.txt', 'r') as myfile2:
    content2 = myfile2.read()

print(content2)

with open('./resources/vegetables.txt', 'w') as vegetables:
    vegetables.write('Tomato\nCucumber\nOnion\n')
    vegetables.write('Gallic\n')

with open('./resources/vegetables.txt', 'a+') as vegetables:
    vegetables.write('Okra')
    vegetables.seek(0)
    content = vegetables.read()

print(content)



