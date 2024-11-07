# routing.py
from collections import defaultdict

class DistanceVectorRouting:
    def __init__(self, routers):
        self.routers = routers
        self.routing_table = defaultdict(dict)
        self.initialize_routing()

    def initialize_routing(self):
        for router in self.routers:
            # Inicializa as tabelas de roteamento com distâncias infinitas
            self.routing_table[router] = {neighbor: float('inf') for neighbor in self.routers}
            self.routing_table[router][router] = 0  # Distância para si mesmo é 0

    def update_route(self, router, destination, distance):
        self.routing_table[router][destination] = distance

    def get_best_route(self, router, destination):
        # Para compatibilidade com Python 3.5, não usamos f-string
        return min(self.routing_table[router], key=lambda x: self.routing_table[router][x])

    def share_routing_info(self):
        # Simula a troca de informações entre roteadores vizinhos
        for router in self.routers:
            for neighbor in self.routers:
                if router != neighbor:
                    # Aqui você implementaria a lógica de atualização da tabela de roteamento
                    pass

    def display_routing_table(self):
        for router, table in self.routing_table.items():
            print("Roteador {}:".format(router))  # Mudado para string formatada compatível com Python 3.5
            for destination, distance in table.items():
                print("\tDestino: {}, Distância: {}".format(destination, distance))  # Mesmo ajuste

class LinkStateRouting:
    def __init__(self, routers):
        self.routers = routers
        self.topology = defaultdict(list)
        self.initialize_topology()

    def initialize_topology(self):
        # Inicializa a topologia completa para cada roteador
        for router in self.routers:
            self.topology[router] = []

    def add_link(self, router1, router2):
        self.topology[router1].append(router2)
        self.topology[router2].append(router1)

    def update_topology(self, router, link):
        # Atualiza a topologia com informações de enlaces
        pass

    def display_topology(self):
        for router, neighbors in self.topology.items():
            print("Roteador {} está conectado a {}".format(router, ', '.join(neighbors)))  # Ajuste similar
