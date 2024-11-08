import heapq
from mininet.net import Mininet
from scapy.all import *
import threading
import time

# Basic structure of a distance-vector router
class DistanceVectorRouter:
    def __init__(self, node, net):
        self.node = node
        self.routing_table = {}  # format: {destination: (next_hop, cost)}
        self.neighbors = net[self.node].connectionsTo(net.hosts)
        self.lock = threading.Lock()
        self.periodic_update()

    def initialize_table(self):
        # Direct connections initialization
        for neighbor, intf in self.neighbors:
            self.routing_table[neighbor] = (neighbor, 1)

    def receive_update(self, packet):
        # Parse and process the distance vector received from neighbors
        pass

    def send_update(self):
        with self.lock:
            for neighbor, _ in self.neighbors:
                packet = self.create_update_packet()
                self.node.cmd('ping -c 1 {}'.format(neighbor.IP()))
                send(packet)

    def periodic_update(self):
        # Send routing table updates periodically
        threading.Timer(10.0, self.periodic_update).start()
        self.send_update()

    def create_update_packet(self):
        # Construct packet containing distance-vector information
        packet = IP(dst="255.255.255.255") / UDP() / "DistanceVectorRouting"
        return packet

    def display_routing_table(self):
        print("\nRouting Table for {}:".format(self.node.name))
        print("Destination\tNext Hop\tCost")
        with self.lock:
            for destination, (next_hop, cost) in self.routing_table.items():
                print("{}\t{}\t{}".format(destination, next_hop, cost))

    def periodic_display(self):
        # Display routing table every 15 seconds
        self.display_routing_table()
        threading.Timer(15.0, self.periodic_display).start()

# Main Mininet setup
def distance_vector_topology():
    net = Mininet()
    net.start()
    routers = [DistanceVectorRouter(node, net) for node in net.hosts]

    try:
        for router in routers:
            router.initialize_table()
            router.periodic_display()  # Starts the periodic display
    except KeyboardInterrupt:
        net.stop()

class LinkStateRouter:
    def __init__(self, node, net):
        self.node = node
        self.net = net
        self.routing_table = {}
        self.neighbor_costs = {neighbor: 1 for neighbor, _ in net[self.node].connectionsTo(net.hosts)}
        self.lsa_database = {}  # format: {node: {neighbor: cost}}
        self.lock = threading.Lock()
        self.broadcast_lsa()

    def broadcast_lsa(self):
        # Broadcasts LSA with neighbor information
        lsa_packet = self.create_lsa_packet()
        for neighbor, _ in self.neighbor_costs.items():
            send(lsa_packet, iface=self.node.defaultIntf().name)
        threading.Timer(10.0, self.broadcast_lsa).start()

    def create_lsa_packet(self):
        # Create a packet with link-state information
        return IP(dst="255.255.255.255") / UDP() / "LinkStateAdvertisement"

    def receive_lsa(self, packet):
        # Process incoming LSAs from neighbors
        pass

    def update_routing_table(self):
        # Implement Dijkstra's algorithm to compute shortest paths
        pass

    def periodic_check(self):
        # Periodically check for any changes in the network state
        threading.Timer(5.0, self.periodic_check).start()
        self.update_routing_table()

    def display_routing_table(self):
        print("\nRouting Table for {}:".format(self.node.name))
        print("Destination\tNext Hop\tCost")
        with self.lock:
            for destination, (next_hop, cost) in self.routing_table.items():
                print("{}\t{}\t{}".format(destination, next_hop, cost))

    def display_lsa_database(self):
        print("\nLSA Database for {}:".format(self.node.name))
        print("Node\tNeighbor\tCost")
        with self.lock:
            for node, neighbors in self.lsa_database.items():
                for neighbor, cost in neighbors.items():
                    print("{}\t{}\t{}".format(node, neighbor, cost))

    def periodic_display(self):
        # Display routing table and LSA database every 15 seconds
        self.display_routing_table()
        self.display_lsa_database()
        threading.Timer(15.0, self.periodic_display).start()

def link_state_topology():
    net = Mininet()
    net.start()
    routers = [LinkStateRouter(node, net) for node in net.hosts]

    try:
        for router in routers:
            router.periodic_display()  # Starts the periodic display
    except KeyboardInterrupt:
        net.stop()
