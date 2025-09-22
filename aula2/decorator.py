def header(function):
    def decorator(nome):
        print(" ##### Bem vindo ao meu Site! #####")
        print("")
        return function(nome)
    return decorator


def footer(function):
    def decorator(nome):
        print("### Copyriter #### ")
        return function(nome)
    return decorator

@header
def produto(nome):
    print(f"Produto: {nome} = R$ 2k")

@header
def sobre():
    print("Esse e minha loja")

produto("Computadpr")
produto("Cadeira Gamer")

    
