print("Bem vindo a sorveteria do João!")

sorvete = []

def adicionarSabor(sorvete):
    adicionar = str(input("Digite o nome do sorvete que queres adicionar: "))
    sorvete.append(adicionar)
    print(f"Você adicionou o sabor {adicionar} no seu sorvete tem {sorvete} de sabores!")

    if len(sorvete) == 4:
        print(removerSabor(sorvete))

    return f"Sorvete de {sorvete} feito com sucesso!"

def removerSabor(sorvete):
    remove = str(input(f"Seu sorvete tem {sorvete} de sabores, qual você deseja excluir: "))
    sorvete.remove(remove)

    return f"Sabor {remove} removido do sorvete, sabores restantes: {sorvete}"

def visualizarSorvete(sorvete):
    return f"Seu sorvete está assim: {sorvete}"

def finalizarPedido(sorvete):
    return(f"Pedido finalizado com sucesso! Seu sorvete ficou com os sabores: {sorvete}")

try:
    while len(sorvete) < 4:
        opcao = int(input("1. Adicionar Sabor\n2. Remover Sabor\n3. Visualizar Sorvete\n4. Finalizar Pedido\nEscolha uma opção:"))

        match opcao:
            case 1:
                print(adicionarSabor(sorvete))
            case 2:
                print(removerSabor(sorvete))
            case 3:
                print(visualizarSorvete(sorvete))
            case 4:
                print(finalizarPedido(sorvete))
                break
            case other:
                print("Você não digitou uma opção válida!\nDigite um número de 1 a 4.")
except ValueError:
    print("Valor inválido!")





    