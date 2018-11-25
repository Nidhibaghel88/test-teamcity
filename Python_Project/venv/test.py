status_map = {'Luke': 'Jedi Knight',
              'Per': 'Pythonist'}

person = 'Luke'

a = person, status_map.get(person, 'unknown')
print(a)



name = input("What's your name?")
print("Nice to meet you " + name + "!")
age = input("Your age? ")
print("So, you are already " + str(age) + " years old, " + name + "!")
