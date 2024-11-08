# create_network.py
import argparse
from topologies import LineTopology, RingTopology, StarTopology, MeshTopology, HybridTopology
from algorithms import DistanceVector, LinkState
from mininet.net import Mininet

def parse_args():
    parser = argparse.ArgumentParser(description="Run network simulation with specified topology and routing algorithm.")
    parser.add_argument('-t', '--topology', choices=['line', 'ring', 'star', 'mesh', 'hybrid'], required=True, help="Choose the network topology.")
    parser.add_argument('-a', '--algorithm', choices=['distance-vector', 'link-state'], required=True, help="Choose the routing algorithm.")
    return parser.parse_args()

def create_topology(topology_name):
    if topology_name == 'line':
        return LineTopology()
    elif topology_name == 'ring':
        return RingTopology()
    elif topology_name == 'star':
        return StarTopology()
    elif topology_name == 'mesh':
        return MeshTopology()
    elif topology_name == 'hybrid':
        return HybridTopology()
    else:
        raise ValueError("Invalid topology name")

def main():
    args = parse_args()
    net = Mininet()
    
    # Set up topology
    topology = create_topology(args.topology)
    topology.build()
    
    # Choose the routing algorithm
    if args.algorithm == 'distance-vector':
        algorithm = DistanceVector(net)
    elif args.algorithm == 'link-state':
        algorithm = LinkState(net)
    else:
        raise ValueError("Invalid algorithm name")
    
    # Run the chosen routing algorithm
    algorithm.run()
    
    # Start the network
    net.start()
    net.pingAll()  # Test connectivity

    print("Testing packet transmission...")
    for i, host in enumerate(net.hosts):
        dest_ip = net.hosts[(i + 1) % len(net.hosts)].IP()  # Get IP of next host
        print("Host {} sending packet to {}".format(host.IP(), dest_ip))
        host.send_packet(dest_ip)

    net.stop()

if __name__ == '__main__':
    main()
