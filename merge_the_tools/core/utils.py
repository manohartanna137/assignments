def merge_tools(strings, k):
    for i in range(0, len(strings), k):
        sub_string = ''
        for j in range(k):
            if strings[i + j] not in sub_string:
                sub_string = sub_string + strings[i + j]
            else:
                continue
        print(sub_string)
    return sub_string