def list_methods(i):
    l = []
    for x in i:
        s = x.split()
        if s[0] == 'insert':
            l.insert(int(s[1]), int(s[2]))
        elif s[0] == 'remove':
            l.remove(int(s[1]))
        elif s[0] == 'append':
            l.append(int(s[1]))
        elif s[0] == 'sort':
            l.sort()
        elif s[0] == 'pop':
            l.pop()
        elif s[0] == 'reverse':
            l.reverse()
        elif s[0] == 'print':
            print(l)

    return l