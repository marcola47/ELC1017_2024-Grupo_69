# algorithms.py
import time
from mininet.node import Host

class DistanceVectorRouting:
    def __init__(self, network):
        self.network = network
        self.routing_tables = {}

    def update_routing_table(self, host):
        """ Update the distance vector for the host """
        # Simple example for distance vector
        routing_table = {host: {} for host in self.network.hosts}
        for h in self.network.hosts:
            if h != host:
                # Here you can implement your distance-vector logic (simplified for this example)
                routing_table[h] = {'next_hop': h, 'distance': 1}
        self.routing_tables[host] = routing_table

    def print_routing_table(self):
        """ Print the routing table for each host in a human-readable format """
        for host in self.network.hosts:
            print("Routing table for {} ({}):".format(host.name, host.IP()))
            for dest, info in self.routing_tables[host].items():
                next_hop = info.get('next_hop', 'N/A')
                distance = info.get('distance', 'N/A')
                # If next_hop is a Host object, extract its name and IP
                if isinstance(next_hop, Host):
                    next_hop_name = next_hop.name
                    next_hop_ip = next_hop.IP()
                else:
                    next_hop_name = next_hop
                    next_hop_ip = 'N/A'
                print("  Destination: {} ({}), Next Hop: {} ({}), Distance: {}".format(
                    dest.name, dest.IP(), next_hop_name, next_hop_ip, distance))
            print()  # Add a newline between each host's routing table

    def run(self):
        """Simulate Distance Vector algorithm for each host"""
        for host in self.network.hosts:
            self.update_routing_table(host)
        self.print_routing_table()
        print("Distance Vector routing tables updated.")


class LinkStateRouting:
    def __init__(self, network):
        self.network = network
        self.routing_tables = {}

    def update_routing_table(self, host):
        """ Update the link-state routing table for the host """
        # Example link-state routing, where each host has its full view of the network
        routing_table = {host: {} for host in self.network.hosts}
        for h in self.network.hosts:
            if h != host:
                # Simplified for illustration: set direct link distance
                routing_table[h] = {'next_hop': h, 'distance': 1}
        self.routing_tables[host] = routing_table

    def run(self):
        """Simulate Link-State algorithm for each host"""
        for host in self.network.hosts:
            self.update_routing_table(host)
            print("Link State routing table for {}: {}".format(host.name, self.routing_tables[host]))
        print("Link State routing tables updated.")

