def search_replace(my_list, search, replace):
    if my_list is not None:
        new = []
        new = my_list.copy()
        for i in range(len(my_list)):
            if new[i] == search:
                new.pop(i)
                new.insert(i, replace)
        return new
