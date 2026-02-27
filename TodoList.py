choice = True
show = []

while choice:
    task = input("What task do you want to do? ")
    show.append(task)  # Add full task to list

    user = input("Want to add more? (yes/no) ")
    if user.lower() == 'no':
        choice = False

print("Your To-Do List:")
for t in show:
    print("-", t)