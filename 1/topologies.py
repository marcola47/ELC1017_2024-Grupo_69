# topologies.py
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel

class LineTopo(Topo):
    def build(self):
        # Create a linear topology
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 5)]  # 4 switches
        hosts = [self.addHost('h{}'.format(i)) for i in range(1, 6)]  # 5 hosts
        
        # Connect hosts to switches
        self.addLink(hosts[0], switches[0])  # h1 to s1
        for i in range(1, 4):  # Connect switches in a line and hosts to them
            self.addLink(switches[i - 1], switches[i])
            self.addLink(hosts[i], switches[i])
        self.addLink(switches[3], hosts[4])  # Connect s4 to h5

class RingTopo(Topo):
    def build(self):
        # Create a ring topology
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 6)]
        hosts = [self.addHost('h{}'.format(i)) for i in range(1, 6)]
        
        # Connect hosts to switches
        for i in range(4):
            self.addLink(hosts[i], switches[i])
            self.addLink(switches[i], switches[i + 1])
        
        self.addLink(hosts[4], switches[4])
        self.addLink(switches[4], switches[0])

class StarTopo(Topo):
    def build(self):
        # Create a star topology
        switch = self.addSwitch('s1')
        hosts = [self.addHost('h{}'.format(i)) for i in range(1, 6)]
        
        # Connect hosts to the central switch
        for host in hosts:
            self.addLink(host, switch)

class MeshTopo(Topo):
    def build(self):
        # Create a mesh topology (fully connected)
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 6)]
        hosts = [self.addHost('h{}'.format(i)) for i in range(1, 6)]
        
        # Connect hosts to switches
        for i in range(5):
            self.addLink(hosts[i], switches[i])
        
        # Fully connect the switches
        for i in range(5):
            for j in range(i+1, 5):
                self.addLink(switches[i], switches[j])

class HybridTopo(Topo):
    def build(self):
        # Hybrid topology: combine a star and a mesh
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 6)]
        hosts = [self.addHost('h{}'.format(i)) for i in range(1, 6)]
        
        # Star part
        center_switch = self.addSwitch('s1')
        for host in hosts:
            self.addLink(host, center_switch)
        
        # Mesh part
        for i in range(5):
            for j in range(i+1, 5):
                self.addLink(switches[i], switches[j])

def create_network(topology):
    """Creates and returns the network based on the topology."""
    net = Mininet(topo=topology, controller=Controller, switch=OVSKernelSwitch)
    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
