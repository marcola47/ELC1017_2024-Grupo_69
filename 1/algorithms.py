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

    def get_neighbors(self, host):
        """ Get neighbors of a host and their link costs """
        neighbors = []
        for link in host.connections():
            # Get the connected host from the link
            neighbor = link[0] if link[1] == host else link[1]
            # Assume random distances for simplicity. Replace with real link costs if available
            link_cost = random.randint(1, 10)  # Link cost
            neighbors.append((neighbor, link_cost))
        return neighbors

    def calculate_shortest_path(self, source):
        """ Calculate the shortest paths from the source to all other hosts using Dijkstra's algorithm """
        # Initialize distances and previous nodes
        distances = {host: float('inf') for host in self.network.hosts}
        previous_nodes = {host: None for host in self.network.hosts}
        distances[source] = 0
        unvisited_hosts = [(0, source)]  # (distance, host)

        while unvisited_hosts:
            current_distance, current_host = heapq.heappop(unvisited_hosts)

            # Skip if this host has already been visited
            if current_distance > distances[current_host]:
                continue

            # Get neighbors and update their distances
            for neighbor, link_cost in self.get_neighbors(current_host):
                new_distance = current_distance + link_cost
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_host
                    heapq.heappush(unvisited_hosts, (new_distance, neighbor))

        return distances, previous_nodes

    def update_routing_table(self, host):
        """ Update the routing table for the host based on the SPF algorithm """
        distances, previous_nodes = self.calculate_shortest_path(host)
        routing_table = {}
        for destination, distance in distances.items():
            # Determine the next hop by following the previous nodes
            if destination != host:
                next_hop = destination
                while previous_nodes[next_hop] and previous_nodes[next_hop] != host:
                    next_hop = previous_nodes[next_hop]
                routing_table[destination] = {'next_hop': next_hop, 'distance': distance}
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
        """ Simulate the SPF (Dijkstra) algorithm for each host in the network """
        for host in self.network.hosts:
            self.update_routing_table(host)
        self.print_routing_table()
        print("SPF (Dijkstra) routing tables updated.")
