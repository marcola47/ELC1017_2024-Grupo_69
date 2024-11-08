# algorithms.py
from scapy.all import Ether, IP, UDP, sendp
from mininet.net import Mininet

class DistanceVector:
    def __init__(self, net):
        self.net = net
        self.routing_table = {}

    def run(self):
        """
        Implement the Distance Vector algorithm:
        Each router maintains a table of the shortest distances to all other nodes.
        The routers exchange their distance tables with each other to update their own table.
        """
        # Initialize routing tables for each host
        for host in self.net.hosts:
            self.routing_table[host] = {}
            for neighbor in self.net.hosts:
                if host != neighbor:
                    self.routing_table[host][neighbor] = 1  # Assuming direct neighbors have distance 1
                else:
                    self.routing_table[host][neighbor] = 0  # Distance to itself is 0

        # Simulate distance vector exchange between routers
        # In a real implementation, routers would periodically send their tables to neighbors
        print("Distance Vector Routing Initialized.")
        
        # For this example, let's assume that the distances to direct neighbors are known and that the routers update their tables
        for host in self.net.hosts:
            print("Routing Table for Host {}:".format(host.IP()))
            for destination, distance in self.routing_table[host].items():
                print("  Destination: {}, Distance: {}".format(destination.IP(), distance))

        # Here, you'd implement the actual updates based on received distance vectors

class LinkState:
    def __init__(self, net):
        self.net = net
        self.link_state_db = {}

    def run(self):
        """
        Implement the Link State algorithm:
        Each router broadcasts its link state to all other routers, and they calculate the shortest paths.
        """
        # Initialize the link-state database for each host
        for host in self.net.hosts:
            self.link_state_db[host] = {}
            # For simplicity, let's assume each router has the state of its directly connected links
            for neighbor in self.net.hosts:
                if host != neighbor:
                    self.link_state_db[host][neighbor] = 1  # Assuming direct links have state 1
                else:
                    self.link_state_db[host][neighbor] = 0  # Link to itself is state 0

        # Simulate link-state advertisement between routers
        # Normally, routers broadcast link-state packets (LSAs) to all other routers
        print("Link State Routing Initialized.")

        # Display link state databases
        for host in self.net.hosts:
            print("Link-State DB for Host {}:".format(host.IP()))
            for neighbor, state in self.link_state_db[host].items():
                print("  Neighbor: {}, Link State: {}".format(neighbor.IP(), state))

        # In a real-world scenario, routers would compute the shortest path tree based on their link-state database
        # For now, we are simply printing out the link states of the network

        # Example of sending a link-state packet using Scapy (used for simulation here)
        # In real routing, this would be more complex, involving flooding and SPF calculations
        for host in self.net.hosts:
            dest_ip = self.net.hosts[(self.net.hosts.index(host) + 1) % len(self.net.hosts)].IP()
            self.send_link_state_packet(host, dest_ip)

    def send_link_state_packet(self, host, dest_ip):
        """Simulate the sending of a link-state advertisement (LSA)"""
        pkt = Ether() / IP(dst=dest_ip) / UDP(dport=5000)  # Assume LSA sent over UDP port 5000
        print("Host {} sending link-state packet to {}".format(host.IP(), dest_ip))
        sendp(pkt, iface=host.defaultIntf(), verbose=False)
