import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from topologies import setup_line_topology, setup_ring_topology, setup_star_topology, setup_mesh_topology, setup_hybrid_topology
import argparse

def main():
    parser = argparse.ArgumentParser(description="Configuração de topologias no Mininet")
    parser.add_argument('-t', dest='topology', choices=['line', 'ring', 'star', 'mesh', 'hybrid'], required=True, help="topology type")
    args = parser.parse_args()

    if args.topology == 'line':
        setup_line_topology()
    elif args.topology == 'ring':
        setup_ring_topology()
    elif args.topology == 'star':
        setup_star_topology()
    elif args.topology == 'mesh':
        setup_mesh_topology()
    elif args.topology == 'hybrid':
        setup_hybrid_topology()

if __name__ == "__main__":
    main()
