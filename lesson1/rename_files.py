import os


def rename_file():
    save_cur_path = os.getcwd()
    os.chdir(r"/home/aria/Desktop/prank")
    file_list = os.listdir("./")

    for oldName in file_list:
        new_name = "".join([cur_letter for cur_letter in oldName if not cur_letter.isdigit()])
        os.renames(oldName, new_name)

    os.chdir(save_cur_path)


def rename_file_second_version():
    save_cur_path = os.getcwd()
    os.chdir(r"/home/aria/Desktop/prank2")
    file_list = os.listdir("./")

    for oldName in file_list:
        print oldName
        print oldName.translate(None, "0123456789")
        print "-------------------------------------"
        os.renames(oldName, oldName.translate(None, "0123456789"))

    os.chdir(save_cur_path)


rename_file()
rename_file_second_version()
