# main.py
import argparse
from mininet.net import Mininet
from mininet.node import Controller
from topologies import LineTopo, RingTopo, StarTopo, MeshTopo, HybridTopo
from algorithms import DistanceVectorRouting, LinkStateRouting, FloodingRouting

def main():
    parser = argparse.ArgumentParser(description="Network Topology and Routing Algorithm Simulation")
    parser.add_argument("-t", "--topology", choices=['line', 'ring', 'star', 'mesh', 'hybrid'], required=True, help="Topology type")
    parser.add_argument("-a", "--algorithm", choices=['distance-vector', 'link-state', 'flooding'], required=True, help="Routing algorithm")

    args = parser.parse_args()

    # Select topology
    if args.topology == 'line':
        topology = LineTopo()
    elif args.topology == 'ring':
        topology = RingTopo()
    elif args.topology == 'star':
        topology = StarTopo()
    elif args.topology == 'mesh':
        topology = MeshTopo()
    elif args.topology == 'hybrid':
        topology = HybridTopo()

    # Create and start the network
    net = Mininet(topo=topology, controller=Controller)
    net.start()

    # Select routing algorithm
    if args.algorithm == 'distance-vector':
        algorithm = DistanceVectorRouting(net)
    elif args.algorithm == 'link-state':
        algorithm = LinkStateRouting(net)
    elif args.algorithm == 'flooding':
        algorithm = FloodingRouting(net)

    # Run the selected routing algorithm
    algorithm.run()

    # Run the CLI to interact with the network
    from mininet.cli import CLI
    CLI(net)

    # Stop the network
    net.stop()

if __name__ == "__main__":
    main()
