def mutate_string(string, position, character):
    a=string
    c=a[:position]+character+a[position:]
    return c