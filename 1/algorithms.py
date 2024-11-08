import random
import heapq
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
                routing_table[h] = {'next_hop': h, 'distance': random.randint(1, 10)}
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
                routing_table[h] = {'next_hop': h, 'distance': random.randint(1, 10)}
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
        """Simulate Link-State algorithm for each host"""
        for host in self.network.hosts:
            self.update_routing_table(host)
        self.print_routing_table()
        print("Link State routing tables updated.")

import random
import heapq
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
                routing_table[h] = {'next_hop': h, 'distance': random.randint(1, 10)}
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
                routing_table[h] = {'next_hop': h, 'distance': random.randint(1, 10)}
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
        """Simulate Link-State algorithm for each host"""
        for host in self.network.hosts:
            self.update_routing_table(host)
        self.print_routing_table()
        print("Link State routing tables updated.")

class SpfRouting:
    def __init__(self, network):
        self.network = network
        self.routing_tables = {}

    def update_routing_table(self, host):
        """ Update the SPF (Shortest Path First) routing table for the host using Dijkstra's algorithm """
        # Create a graph where nodes are hosts and edges are link distances (random for now)
        graph = {h: {} for h in self.network.hosts}
        for h1 in self.network.hosts:
            for h2 in self.network.hosts:
                if h1 != h2:
                    graph[h1][h2] = random.randint(1, 10)  # Random link distance for now

        # Dijkstra's algorithm to compute shortest paths from the host
        distances = {h: float('inf') for h in self.network.hosts}
        previous_nodes = {h: None for h in self.network.hosts}
        distances[host] = 0
        pq = [(0, host)]  # priority queue of (distance, node)

        while pq:
            current_distance, current_node = heapq.heappop(pq)
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Build the routing table based on the shortest paths
        routing_table = {}
        for dest in self.network.hosts:
            if dest != host:
                next_hop = previous_nodes[dest]
                routing_table[dest] = {'next_hop': next_hop, 'distance': distances[dest]}

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
        """Simulate SPF algorithm for each host"""
        for host in self.network.hosts:
            self.update_routing_table(host)
        self.print_routing_table()
        print("SPF routing tables updated.")
