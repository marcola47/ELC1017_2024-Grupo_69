from mininet.net import Mininet
from mininet.node import Controller, OVSSwitch
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel

def setup_line_topology():
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)
    net.addController('c0')

    # Adiciona nós (roteadores)
    routers = [net.addSwitch(f'r{i}') for i in range(5)]
    hosts = [net.addHost(f'h{i}') for i in range(5)]

    # Cria conexões em linha
    for i in range(4):
        net.addLink(routers[i], routers[i + 1], bw=10)  # largura de banda configurável
        net.addLink(routers[i], hosts[i])
    
    net.addLink(routers[4], hosts[4])

    net.start()
    CLI(net)
    net.stop()

def setup_ring_topology():
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)
    net.addController('c0')

    routers = [net.addSwitch(f'r{i}') for i in range(5)]
    hosts = [net.addHost(f'h{i}') for i in range(5)]

    for i in range(5):
        net.addLink(routers[i], routers[(i + 1) % 5], bw=10)
        net.addLink(routers[i], hosts[i])

    net.start()
    CLI(net)
    net.stop()

def setup_star_topology():
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)
    net.addController('c0')

    central_router = net.addSwitch('rc')
    hosts = [net.addHost(f'h{i}') for i in range(5)]

    for i in range(5):
        net.addLink(central_router, hosts[i], bw=10)

    net.start()
    CLI(net)
    net.stop()

def setup_mesh_topology():
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)
    net.addController('c0')

    routers = [net.addSwitch(f'r{i}') for i in range(4)]
    hosts = [net.addHost(f'h{i}') for i in range(4)]

    # Conexão em malha completa entre os roteadores
    for i in range(4):
        for j in range(i + 1, 4):
            net.addLink(routers[i], routers[j], bw=10)

    for i in range(4):
        net.addLink(routers[i], hosts[i])

    net.start()
    CLI(net)
    net.stop()

def setup_hybrid_topology():
    net = Mininet(controller=Controller, link=TCLink, switch=OVSSwitch)
    net.addController('c0')

    # Roteadores centrais
    central_router = net.addSwitch('rc')
    sub_routers = [net.addSwitch(f'r{i}') for i in range(3)]
    hosts = [net.addHost(f'h{i}') for i in range(6)]

    # Conexão estrela no centro
    for router in sub_routers:
        net.addLink(central_router, router, bw=10)

    # Conexão em linha para alguns hosts em cada sub-rede
    for i, router in enumerate(sub_routers):
        net.addLink(router, hosts[i * 2])
        net.addLink(router, hosts[i * 2 + 1])

    net.start()
    CLI(net)
    net.stop()