choice = input("\
 Options\n\
 1 = break\n\
 2 = pass \n\
 3 = continue\n\
 4 = for with else\n\
 5 = while with else \n\
Choose an option :")

if choice == "1":
    for i in range(10):
        if i == 5:
            break
        print(i)
elif choice == "2":
    for i in range(5):
        pass
elif choice == "3":
    for i in range(5):
        if i == 3:
            continue
        print(i)
elif choice == "4":
    for i in range(5):
        print(i)
    else:
        print("Loop completed!")
elif choice == "5":
    i = 0
    while i < 5:
        print(i)
        i += 1
    else:
        print("Loop completed!")
else:
    print("Invalid choice!")


