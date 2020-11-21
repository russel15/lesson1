# x = 0
# while x < 10:
#     print(x)
#     x += 1


def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return one+delimiter+two

print(str.upper(get_summ("Learn", "python")))