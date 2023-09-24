def idade(num=0):
    hello(str(num) + ' anos')

def hello(nome=""):
    x = "" if nome=="" else ", " + nome
    print(f"Hello {x}!")

hello('fafm')
idade('fabricio ' + str(45))