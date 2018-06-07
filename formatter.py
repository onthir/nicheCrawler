import os
def do_it(user):
    

    u = str((user).lower()).replace(" ", "-")
    file_to_read = (str(user).lower()) + "/" + str(u) + "-universities.txt"

    file_to_write = (str(user).lower()) + "/formatted.txt"

    with open(file_to_read, 'r') as file:
        f = file.readlines()
        for r in f:
            b = r.lower()
            c = b.replace(" ", "-")
            d = c.replace("\n", "")
            
            # write to the file
            with open(file_to_write, 'a') as fl:
                fl.writelines(d + "\n")
                print(str(r) + " --> Done")