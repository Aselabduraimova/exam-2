def func2(*args):
    summa = 0
    for number in args:
        if isinstance(number, (int,float)):
            summa += number
    return summa

print(func2(10,'bbdbsknsv',5.7))





results_list = []
def func3(text, word):
    text.upper()
    word.upper()
    for item in text.split():
        if item.startwith(word):
            results_list.append(item)
    return results_list
