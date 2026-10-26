# Adicionado 'refrigerante' direto na lista inicial
cardapio = ['pastel', 'pizza', 'coxinha', 'refrigerante']

print(f"itens do cardapio {cardapio}")
pedido = input("O que você quer comer hoje? ")

if pedido in cardapio:
    print(f"{pedido} está no cardapio.")
else:
    print(f"{pedido} nao esta no cardapio.")
    
    # Pergunta se quer adicionar o item novo
    adicionar = input(f"Deseja adicionar {pedido} ao cardápio? (sim/nao): ")
    if adicionar == "sim":
        cardapio.append(pedido)
        print(f"Pronto! {pedido} foi adicionado.")
        print(f"Novo cardapio: {cardapio}")

# Cardápio updated conforme o terminal da sua imagem
cardapio = ['pastel', 'pizza', 'coxinha', 'refrigerante', 'caldo de cana']

print(f"itens do cardapio {cardapio}")
pedido = input("O que você quer tirar do cardápio hoje? ")

if pedido in cardapio:
    print(f"{pedido} está no cardapio.")
    
    # Pergunta se quer remover o item existente
    remover = input(f"Deseja remover {pedido} do cardápio? (sim/nao): ")
    if remover == "sim":
        cardapio.remove(pedido)  # <--- O remove entra aqui!
        print(f"Pronto! {pedido} foi removido.")
        print(f"Novo cardapio: {cardapio}")
else:
    print(f"{pedido} nao esta no cardapio, então não pode ser removido.")

# NOVO BLOCO: Testando o método insert no final do script
print("\n--- Testando a Inserção por Posição (Insert) ---")
print(f"Cardápio atual: {cardapio}")
novo_item = input("Digite um novo item para inserir em uma posição específica: ")
posicao = int(input("Em qual posição do cardápio você quer inserir? "))

# O método insert insere o item exatamente no índice desejado
cardapio.insert(posicao, novo_item)

print(f"Pronto! '{novo_item}' foi inserido na posição {posicao}.")
print(f"Cardápio final: {cardapio}")


# ULTIMO BLOCO: Testando o método pop no encerramento do script (Sem operadores matemáticos)
print("\n--- Testando a Remoção por Índice (Pop) ---")
print(f"Cardápio antes do pop: {cardapio}")

# Pede ao usuário a posição numérica do item diretamente, olhando a lista impressa na tela
indice_remover = int(input("Escolha um índice do cardápio acima para remover via pop: "))

# O pop remove o item da posição e o guarda na variável 'item_removido'
item_removido = cardapio.pop(indice_remover)

print(f"Pronto! O item '{item_removido}' foi retirado usando pop.")
print(f"Cardápio atualizado: {cardapio}")
