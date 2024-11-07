def simulate_link_failures(net, r1, r2, r3):
    print("Simulando falhas de enlace e mudanças de topologia...")

    # Desconecta o link entre r1 e r2
    print("Desconectando link entre r1 e r2")
    net.configLinkStatus('r1', 'r2', 'down')
    time.sleep(5)  # Aguarda 5 segundos

    # Reconecta o link entre r1 e r2
    print("Reconectando link entre r1 e r2")
    net.configLinkStatus('r1', 'r2', 'up')
    time.sleep(5)

    # Desconecta o link entre r2 e r3
    print("Desconectando link entre r2 e r3")
    net.configLinkStatus('r2', 'r3', 'down')
    time.sleep(5)

    # Reconecta o link entre r2 e r3
    print("Reconectando link entre r2 e r3")
    net.configLinkStatus('r2', 'r3', 'up')
    time.sleep(5)

    # Desconecta o link entre r3 e r1
    print("Desconectando link entre r3 e r1")
    net.configLinkStatus('r3', 'r1', 'down')
    time.sleep(5)

    # Reconecta o link entre r3 e r1
    print("Reconectando link entre r3 e r1")
    net.configLinkStatus('r3', 'r1', 'up')
    print("Simulação de falhas de enlace concluída.")

def simulate_topology_changes(net, r1, r2, r3):
    # Adiciona um novo link entre r1 e r3, simulando uma rota alternativa
    print("Adicionando novo link entre r1 e r3")
    net.addLink(r1, r3, bw=5)
    time.sleep(5)

    # Remove o link entre r1 e r3
    print("Removendo link entre r1 e r3")
    net.delLinkBetween(r1, r3)
    time.sleep(5)

    print("Simulação de mudanças de topologia concluída.")


