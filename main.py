def add_to_dict(*args):
    if type(args[0]) != dict:
        print(f"You need to send a dicionary. You sent: {type(args[0])}")

    elif type(args[0]) == dict:
        try:
            if type(args[1]) == str and type(args[2]) == str:
                if args[1] in args[0].keys():
                    print(f"{args[1]} is already on the dictionary. Won't add")
                else:
                    args[0][args[1]] = args[2]
                    print(f"{args[1]} has been added.")
        except:
            print("You need to send a word and a definition.")
    else:
        print("Error")


def get_from_dict(*args):
    if type(args[0]) != dict:
        print(f"You need to send a dicionary. You sent: {type(args[0])}")
    elif type(args[0]) == dict:
        try:
            if type(args[1]) == str:
                if args[1] in args[0].keys():
                    print(f"{args[1]}: {args[0][args[1]]}")
                else:
                    print(f"{args[1]} was not found in this dict.")
        except:
            print("you need to send a word to search for.")
    else:
        print("Error")


def update_word(*args):
    if type(args[0]) != dict:
        print(f"You need to send a dicionary. You sent: {type(args[0])}")
    elif type(args[0]) == dict:
        try:
            if type(args[1]) == str and type(args[2]) == str:
                if args[1] in args[0].keys():
                    args[0][args[1]] = args[2]
                    print(f"{args[1]} has been updated to : {args[2]}")
                else:
                    print(
                        f"{args[1]} is not on the dict. Can't update non-existing word.")
        except:
            print("you need to send a word and a definition to update.")
    else:
        print("Error")


def delete_from_dict(*args):
    if type(args[0]) != dict:
        print(f"You need to send a dicionary. You sent: {type(args[0])}")
    elif type(args[0]) == dict:
        try:
            if type(args[1]) == str:
                if args[1] in args[0].keys():
                    del args[0][args[1]]
                    global delete_list
                    delete_list.append(args[1])
                    print(f"{args[1]} has been deleted.")
                else:
                    if args[1] in delete_list:
                        print(f"{args[1]} was not found in this dict.")
                    else:
                        print(f"{args[1]} is not in this dict. Won't delete.")
        except:
            print("you need to specify a word to delete.")
    else:
        print("Error")


delete_list = []
my_english_dict = {}

print('####add_to_dict####\n')
add_to_dict("hello", "kimchi")
add_to_dict(my_english_dict, "kimchi")
add_to_dict(my_english_dict, "kimchi", "The source of life.")
add_to_dict(my_english_dict, "kimchi", "My fav. food")

print('\n####get_from_dict####\n')
get_from_dict("hello", "kimchi")
get_from_dict(my_english_dict)  # you need to send a word to search for.
get_from_dict(my_english_dict, "galbi")  # galbi was not found in this dict.
get_from_dict(my_english_dict, "kimchi")  # kimchi: The sourche of life.

print('\n####update_word####\n')
update_word("hello", "kimchi")
update_word(my_english_dict, "kimchi")
update_word(my_english_dict, "galbi", "Love it.")
update_word(my_english_dict, "kimchi", "Food from the gods")
get_from_dict(my_english_dict, "kimchi")

print('\n####delete_from_dict####\n')
delete_from_dict("hello", "kimchi")
delete_from_dict(my_english_dict)
delete_from_dict(my_english_dict, "galbi")
delete_from_dict(my_english_dict, "kimchi")
delete_from_dict(my_english_dict, "kimchi")


# test_dict = {"kimchi": "50"}
# if "kimchi" in test_dict.keys():
#     print("true")
# if test_dict["kimchi"] == True:
#     print("True")
