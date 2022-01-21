def func(name,**args):
    print(name)
    for key, value in args.items():
        print(key, "-", value)

func(name='USA', population='330 million', is_democratic=True)