def mutate_string(string, position, character):
    a=string
    c=a[:position]+character+a[position:]
    print(c)
    return c
