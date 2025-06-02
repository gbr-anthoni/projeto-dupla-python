
# python main.py

preparing = [] # Pedidos que estão sendo preparados.

ready = [] # Pedidos que estão prontos.

while True: # loop.
    order = input("order:") # Digitar o número do pedido.

    if order == "sair": # se order for 'sair' ele termina a execulção do programa.
        break

    elif order not in preparing and order not in ready: # se o pedido não estiver em 'preparando' e não estiver em 'pronto'.
        preparing.append(order) # Significa que é um novo pedido e que precisa ser preparado.

    elif order in preparing and order not in ready: # se o pedido estiver em 'preparando' mas não estiver em 'pronto'.
        # significa que é um pedido que está pronto.
        preparing.remove(order) # remover de 'preparando'.
        ready.append(order) # colocar em 'pronto'

    elif order not in preparing and order in ready: # se o pedido não estiver em 'preparando' mas estiver em 'pronto'.
        ready.remove(order) # Significa que o pedido já foi recebido.

    print(preparing,ready)
