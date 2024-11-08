import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))
from topologies import setup_line_topology, setup_ring_topology, setup_star_topology, setup_mesh_topology, setup_hybrid_topology
from routing import DistanceVectorRouting, LinkStateRouting

def main():
    parser = argparse.ArgumentParser(description="Configuração de topologias no Mininet")
    parser.add_argument('-t', dest='topology', choices=['line', 'ring', 'star', 'mesh', 'hybrid'], required=True, help="topology type")
    parser.add_argument('-a', dest='algorithm', choices=['distance-vector', 'link-state'], required=True, help="routing algorithm")
    args = parser.parse_args()

    # Configura a topologia
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

    # Configura o algoritmo de roteamento
    if args.algorithm == 'distance-vector':
        router_algo = DistanceVectorRouting(routers=['r0', 'r1', 'r2', 'r3'])  # Exemplo de roteadores
    elif args.algorithm == 'link-state':
        router_algo = LinkStateRouting(routers=['r0', 'r1', 'r2', 'r3'])

    # Exibe a tabela de roteamento
    router_algo.display_routing_table()

if __name__ == "__main__":
    main()