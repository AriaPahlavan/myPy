import os


# no_int_file_list = [x for x in file_list if not (x.isdigit()
#                                                      or x[0] == '-' and x[1:].isdigit())]

# is_integer = lambda s: not s.isdigit() or (s[0] == '-' and not s[1:].isdigit())
#     no_int_file_list = filter(is_integer, file_list)

def rename_file():
    os.chdir(r"/home/aria/Desktop/prank")
    file_list = os.listdir("./")
    new_list = []

    for oldName in file_list:
        new_name = "".join([cur_letter for cur_letter in oldName if not cur_letter.isdigit()])
        os.renames(oldName, new_name)

    print new_list


rename_file()
