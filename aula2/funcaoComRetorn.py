def msg(header,footer):
    header()
    print("ola muito bem vindo!!")
    footer()
def header():
    print("### Innicio ###")
def footer():
    print("### Fimmmm!!! ####")
msg(header=header,footer=footer)



def soma(a,b):
    resultado = a + b
    return resultado

result = soma(34,56)
header()
print(result)

