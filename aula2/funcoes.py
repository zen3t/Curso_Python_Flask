

def ola(nome,cpf,idade=0,maiuscula=False,*args,**kwargs):
    print(args)
    print(kwargs)
    if maiuscula:
        msg = f'Ola {nome} {cpf} a sua {idade}'.upper()
    else:
        msg = f'Ola {nome}, {cpf} a sua {idade}'

        print(msg)
pessoa = ['ze',857673-57,42]
ola(*pessoa)
pessoas = {
    'nome':'Carla',
    'cpf': '4356787890-654',
    'idade':42
}
ola(**pessoas)
