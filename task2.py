txt = "Advertising companies say advertising is necessary and important. It informs people about new products. Advertising hoardings in the street make our environment colorful. And adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next program in the mini-drama. Advertising can educate, too. Adverts tell us about new, healthy products. And adverts in magazines give us ideas for how to look prettier, be fashionable and be successful. Without advertising, life is boring and colorless. But some consumers argue that advertising is a bad thing. They say that advertising is bad for children. Adverts make children ‘pester’ their parents buy things for them. Advertisers know we love our children and want to give them everything. So they use children’s ‘pester power’ to sell their products. Finally, consumers say, if there is advertising there must be rules. Some adverts advertise unhealthy things like cigarettes and make people waste their money."

def to_upper(string_):
    return string_.upper()
print("Task 2.1")
print(f'{to_upper(txt)} \n')

def counter(text):
    count_let_s=0
    count_let_t=0

    for i in text:
        if i=="s":
            count_let_s+=1
        elif i=="t":
            count_let_t+=1

    return print(f" Task 2.2 \n Количество буквы 's'={count_let_s},буквы 't'={count_let_t}.\n")
counter(txt)




list_ = []
def func3(text, word):
    text.upper()
    word.upper()
    for i in text.split():
        if i.startswith(word):
            list_.append(str.upper(i))

    return list_

print("Task 2.3")
print(func3(txt, 'advert'))
