# topologies.py
from mininet.topo import Topo
from mininet.node import Host
from scapy.all import sendp, Ether, IP, UDP

class ScapyHost(Host):
    def config(self, **params):
        super(ScapyHost, self).config(**params)
        self.cmd('sysctl -w net.ipv4.ip_forward=1')  # Enable IP forwarding
        self.cmd('sysctl -w net.ipv6.conf.all.disable_ipv6=1')  # Disable IPv6
        self.cmd('sysctl -w net.ipv6.conf.default.disable_ipv6=1')  # Disable IPv6 on default interfaces

    def send_packet(self, dest_ip):
        # Create and send a UDP packet using Scapy
        pkt = Ether() / IP(dst=dest_ip) / UDP(dport=80, sport=4000)
        sendp(pkt, iface=self.defaultIntf(), verbose=False)

class LineTopology(Topo):
    def build(self):
        # Create 3 switches and 3 hosts in a line topology
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 4)]
        hosts = [self.addHost('h{}'.format(i), cls=ScapyHost, ip='10.0.0.{}'.format(i)) for i in range(1, 4)]
        
        # Connect hosts and switches in a line configuration
        self.addLink(hosts[0], switches[0])
        self.addLink(switches[0], switches[1])
        self.addLink(switches[1], switches[2])
        self.addLink(switches[2], hosts[2])

class RingTopology(Topo):
    def build(self):
        # Create 3 switches and 3 hosts in a ring topology
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 4)]
        hosts = [self.addHost('h{}'.format(i), cls=ScapyHost, ip='10.0.0.{}'.format(i)) for i in range(1, 4)]

        # Connect hosts to switches
        for i in range(3):
            self.addLink(hosts[i], switches[i])

        # Connect switches in a ring
        for i in range(3):
            self.addLink(switches[i], switches[(i + 1) % 3])

class StarTopology(Topo):
    def build(self):
        # Create one central switch and 3 peripheral hosts
        center_switch = self.addSwitch('s1')
        hosts = [self.addHost('h{}'.format(i), cls=ScapyHost, ip='10.0.0.{}'.format(i)) for i in range(1, 4)]
        
        # Connect each host to the central switch
        for host in hosts:
            self.addLink(host, center_switch)

class MeshTopology(Topo):
    def build(self):
        # Create 4 switches and 4 hosts in a mesh topology
        switches = [self.addSwitch('s{}'.format(i)) for i in range(1, 5)]
        hosts = [self.addHost('h{}'.format(i), cls=ScapyHost) for i in range(1, 5)]
        
        # Connect each host to a switch
        for i in range(4):
            self.addLink(hosts[i], switches[i])
        
        # Connect every switch to every other switch
        for i in range(4):
            for j in range(i + 1, 4):
                self.addLink(switches[i], switches[j])

class HybridTopology(Topo):
    def build(self):
        # Create a combination of mesh and star within the hybrid topology
        center_switch = self.addSwitch('s1')
        additional_switches = [self.addSwitch('s{}'.format(i)) for i in range(2, 5)]
        hosts = [self.addHost('h{}'.format(i), cls=ScapyHost) for i in range(1, 5)]
        
        # Star setup with central switch
        for i in range(2):
            self.addLink(hosts[i], center_switch)
        
        # Connect additional switches to the central switch
        for switch in additional_switches:
            self.addLink(center_switch, switch)

        # Attach remaining hosts to each additional switch
        for i, switch in enumerate(additional_switches):
            self.addLink(hosts[i + 2], switch)
