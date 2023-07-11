def ds(roll_no, name):
    #Create a function named ds with parameters roll_no and name.
    my_list = [roll_no, name]
    my_tuple = (roll_no, name)
    my_set = {roll_no, name}
    my_dict = {'Roll No': roll_no, 'Name': name}

    # Add those parameters in the following data structures:list, tuple, sets and dictionaries
    print("Initial data:")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # After adding values change the values during runtime
    my_list[0] = 100
    my_tuple = (200, 'Sanskruti')
    my_set.add(300)
    my_dict['Roll No'] = 400

    #Updated data
    print("\nUpdated data :")
    print("List:", my_list)
    print("Tuple:", my_tuple)
    print("Set:", my_set)
    print("Dictionary:", my_dict)

    # Delete these data structures
    del my_list
    del my_tuple
    del my_set
    del my_dict

    # Check if deleted
    print("List:", my_list)  # raises error
    print("Tuple:", my_tuple)  # raises error
    print("Set:", my_set)  # raises error
    print("Dictionary:", my_dict)  # raises error

# Call the function with roll_no = 1 and name = "Alice"
ds(1, "Shreya")