if __name__ == '__main__':
    setLogLevel('info')

    # Cria a topologia inicial e obtém os nós
    net, r1, r2, r3 = create_ring_topology()

    try:
        # Simula falhas de enlace
        simulate_link_failures(net, r1, r2, r3)

        # Simula mudanças na topologia
        simulate_topology_changes(net, r1, r2, r3)

        # Entra no CLI para interação adicional
        CLI(net)
    finally:
        # Finaliza a rede
        net.stop()
