# algorithms.py
import time
import random
from mininet.node import Host
from scapy.all import send, IP, ICMP

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

class FloodingRouting:
    def __init__(self, network):
        self.network = network
        self.visited = {}  # Dictionary to track visited hosts

    def send_packet(self, source, dest, packet, ttl=10):
        """
        Flood the packet through the network, sending it to all neighbors
        except the source (to prevent loops).
        """
        self.visited = {}  # Reset visited hosts
        self._flood(source, dest, packet, ttl)

    def _flood(self, current_host, dest, packet, ttl):
        """
        Recursively flood the packet to neighbors until it reaches the destination
        or the TTL expires.
        """
        if ttl <= 0:
            return

        # Mark the current host as visited to avoid loops
        self.visited[current_host] = True

        # Check if destination is reached
        if current_host == dest:
            print(f"Destination reached: {dest.name}")
            return

        # Forward the packet to all neighbors
        for neighbor in current_host.neighbors():
            if neighbor not in self.visited:
                # Create a copy of the packet and decrement TTL
                new_packet = packet.copy()
                send(new_packet, iface=neighbor.name)
                print(f"Sending packet from {current_host.name} to {neighbor.name}")
                self._flood(neighbor, dest, packet, ttl-1)

    def run(self, source, dest, packet):
        """Start flooding from source to destination."""
        self.send_packet(source, dest, packet)
        print("Flooding completed.")