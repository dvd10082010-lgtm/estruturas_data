dict = {

    }

## dicts

def verificar_voto():
    while True:
        try:
            eleitor = input("escreva o seu nome: ")
            while eleitor in dict:
                print("nome já cadastrado")
                eleitor = input("escreva o seu nome: ")
            if eleitor  == "0":
                break
            voto = int(input("escreva o numero de seu candidato: "))
            dict[eleitor] = voto
        except ValueError:
            print('valores não conrrespondente')

verificar_voto()
print(dict)