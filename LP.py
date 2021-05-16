def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    summ = one + delimiter + two
    return summ
s = get_summ('learn', 'Python')
print(s.upper())