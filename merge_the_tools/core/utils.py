def merge_the_tools(string, k):
    list1 = []
    for i in range(0, len(string), k):
        sub_string = ''
        for j in range(k):
            if string[i + j] not in sub_string:
                sub_string = sub_string + string[i + j]
            else:
                continue
        list1.append(sub_string)
    return list1