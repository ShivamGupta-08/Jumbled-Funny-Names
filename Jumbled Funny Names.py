import random
friend_list = []
frist_name = []
last_name =[]
number_of_names = int(input("Enter the the number of friends.\n"))
print(f"Enter the name of your {number_of_names} friends")
for i in range(1, number_of_names + 1):
        names = input()
        friend_list.append(names)

for names_of_friends in friend_list:
        split_names = names_of_friends.split(" ")
        frist_name.append(split_names[0])
        split_names.pop(0)
        listToStr = ' '.join([str(elem) for elem in split_names])
        last_name.append(listToStr)

for n in range(number_of_names):
        random_num1 = random.randint(0,number_of_names-1)
        frist_name[n],frist_name[random_num1] = frist_name[random_num1],frist_name[n]
for n in range(number_of_names):
        random_num2 = random.randint(0,number_of_names-1)
        last_name[n],last_name[random_num2] = last_name[random_num2],last_name[n]
print(last_name)
def convertTuple(tup):
    str = ' '.join(tup)
    return str


results = [ele for ele in (zip(frist_name, last_name))]
for ans in results:
        print(convertTuple(ans))
