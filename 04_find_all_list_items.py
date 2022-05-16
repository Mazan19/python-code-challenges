lst = [[1,2,[1,2,3,2,1, [0,1,2,1] ],4,[1,3]]]
search = 1

finds = list()
tmp_lst = lst

def my_index(lst, search):
    local_list = list()
    for i,x in enumerate(lst):
        if isinstance(x, list):
            d = my_index(x, search)
            for dd in d:
                local_list.append([i, dd])
        else:
            if (x==search):
                local_list.append(i)
    return local_list

print (my_index(lst, search))