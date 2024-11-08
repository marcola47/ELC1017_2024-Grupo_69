import json

class Router:
    def __init__(self, router_id):
        self.router_id = router_id
        self.routing_table = {}  # Estrutura {destino: {"cost": X, "next_hop": Y, "interface": Z}}

    def add_route(self, destination, cost, next_hop, interface):
        """Adiciona ou atualiza uma rota na tabela de roteamento."""
        self.routing_table[destination] = {"cost": cost, "next_hop": next_hop, "interface": interface}

    def show_routing_table(self):
        """Exibe a tabela de roteamento atual."""
        print(f"Tabela de Roteamento do Roteador {self.router_id}")
        print("Destino\t\tCusto\tPróximo Salto\tInterface")
        print("-" * 50)
        for dest, info in self.routing_table.items():
            print(f"{dest}\t\t{info['cost']}\t{info['next_hop']}\t\t{info['interface']}")
        print("-" * 50)

    def save_routing_table(self, filename="routing_table.json"):
        """Salva a tabela de roteamento em um arquivo JSON."""
        with open(filename, "w") as f:
            json.dump(self.routing_table, f)

    def load_routing_table(self, filename="routing_table.json"):
        """Carrega a tabela de roteamento de um arquivo JSON."""
        with open(filename, "r") as f:
            self.routing_table = json.load(f)

class RouterCLI(Router):
    def __init__(self, router_id):
        super().__init__(router_id)

    def edit_route(self):
        """Permite editar ou adicionar uma entrada na tabela de roteamento manualmente."""
        dest = input("Digite o destino (IP ou ID do roteador): ")
        cost = int(input("Digite o custo para o destino: "))
        next_hop = input("Digite o próximo salto (ID do roteador ou IP): ")
        interface = input("Digite a interface de saída: ")

        self.add_route(dest, cost, next_hop, interface)
        print(f"Rota para {dest} atualizada com sucesso.")

    def cli_menu(self):
        """Menu de interface de linha de comando para manipular a tabela de roteamento."""
        while True:
            print("\n--- Interface de Roteador ---")
            print("1. Exibir tabela de roteamento")
            print("2. Editar uma rota")
            print("3. Salvar tabela de roteamento")
            print("4. Carregar tabela de roteamento")
            print("5. Sair")
            choice = input("Escolha uma opção: ")

            if choice == '1':
                self.show_routing_table()
            elif choice == '2':
                self.edit_route()
            elif choice == '3':
                self.save_routing_table()
                print("Tabela de roteamento salva com sucesso.")
            elif choice == '4':
                self.load_routing_table()
                print("Tabela de roteamento carregada com sucesso.")
            elif choice == '5':
                print("Encerrando o roteador.")
                break
            else:
                print("Opção inválida. Tente novamente.")
