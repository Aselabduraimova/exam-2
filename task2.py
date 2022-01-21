text=input()

def counter(text):
    count_let_s=0
    count_let_t=0

    for i in text:
        if i=="s":
            count_let_s+=1
        elif i=="t":
            count_let_t+=1
    return print(f"""Количество буквы 's'={count_let_s},буквы 't'={count_let_t}.""")
counter(text)
