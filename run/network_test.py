if __name__ == '__main__':
    setLogLevel('info')
    net, r1, r2, _ = create_ring_topology()

    try:
        # Gera tráfego TCP e UDP usando IPerf
        generate_traffic_iperf(net, r1, r2, protocol="TCP", duration=10)
        generate_traffic_iperf(net, r1, r2, protocol="UDP", duration=10, bandwidth="2M")

        # Entra na CLI do Mininet para análise manual, se desejado
        CLI(net)
    finally:
        net.stop()
