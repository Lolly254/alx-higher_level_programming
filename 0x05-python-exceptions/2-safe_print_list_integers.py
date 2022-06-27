def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    while True:
        try:
            if index < x:
                print('{:d}'.format(my_list[index]), end='')
                index += 1
                count += 1
            else:
                return count
        except:
            index += 1


