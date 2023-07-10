#break
for i in range(1, 10):
    if i == 6:
        break
    print(i)

#pass
for i in range(1, 10):
    if i == 6:
        pass
    else:
        print(i)

#continue
for i in range(1, 10):
    if i == 6:
        continue
    print(i)

# for loop with else statement
for i in range(1, 11):
    print(i)
else:
    print("Loop completed successfully!")

#while loop with else statement
i = 1
while i <= 10:
    print(i)
    i += 1
else:
    print("Loop completed successfully!")