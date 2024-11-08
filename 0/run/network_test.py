def generate_traffic_iperf(net, src, dst, protocol="TCP", duration=10, bandwidth="1M"):
    """
    Gera tráfego entre dois nós usando IPerf.
    
    Args:
        net: Objeto Mininet.
        src: Nó de origem.
        dst: Nó de destino.
        protocol: "TCP" ou "UDP".
        duration: Duração do teste em segundos.
        bandwidth: Banda para UDP (exemplo: "1M" para 1 Mbps).
    """
    print(f"Iniciando teste IPerf entre {src} e {dst} usando {protocol}")

    # Comando de servidor IPerf
    dst.cmd('iperf -s -p 5001 &')  # Porta padrão para o servidor IPerf
    
    # Define o comando para o cliente, com base no protocolo
    if protocol == "UDP":
        client_cmd = f'iperf -c {dst.IP()} -u -t {duration} -b {bandwidth}'
    else:  # TCP por padrão
        client_cmd = f'iperf -c {dst.IP()} -t {duration}'

    # Executa o cliente IPerf no nó de origem
    src.cmd(client_cmd)
    
    # Para o servidor após o teste
    dst.cmd('kill %iperf')

    print(f"Teste IPerf entre {src} e {dst} concluído.")

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
