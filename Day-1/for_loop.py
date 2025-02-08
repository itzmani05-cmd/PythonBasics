languages = ["swift","python","Js"]
for lang in languages:
    print(lang)
print("End of the loop")

language = "Python"
for x in language:
    print(x)

for i in range(0,4):
    print(i)

languages = ["swift","python","Js"]
for lang in languages:
    if lang == 'Js':
        break
    print(lang)

for lang in languages:
    if lang == 'Js':
        continue
    print(lang)

attribute = ['Light','Tier']
cars = ['Testla','Swift','MI']


for attribute in range(0,3):
    for car in (0,2):
        print(attribute,car)
    print("----")

for _ in range(0,4):
    print('Hello!')


