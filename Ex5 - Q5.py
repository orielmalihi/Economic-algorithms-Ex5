import networkx as nx


class Agent:
    def __init__(self, name, estimates):
        self.name = name
        self.estimates = estimates

    def item_value(self, item_index: int):
        if item_index >= len(self.estimates):
            return
        else:
            return self.estimates[item_index]

    def calculate_bundle(self, bundle):
        total_sum = 0
        for item_index in bundle:
            total_sum += self.item_value(item_index-1)
        return  total_sum


def envy_graph(agents, bundles):
    G = nx.DiGraph()
    for i,current_agent in enumerate(agents):
        current_agent_sum = current_agent.calculate_bundle(bundles[i])
        for j,other_agent in enumerate(agents):
            if i == j:
                continue
            else:
                other_agent_sum = current_agent.calculate_bundle(bundles[j])
                if other_agent_sum > current_agent_sum:
                    G.add_edge(current_agent.name, other_agent.name)
    return G

def print_envy_graph(G):
    print("Envy graph edges:") # ('A','B') is equal to 'A is envy of B'
    for edge in nx.edges(G):
        print(edge)
    if len(nx.edges(G))==0:
        print("No one is jealous..")
    print()


ami = Agent("Ami", [3,2,1])
tami = Agent("Tami", [2,1,3])
rami = Agent("Rami", [1,3,2])

agents = [ami, tami, rami]
bundles = [[3], [2], [1]]

G = envy_graph(agents, bundles)
print_envy_graph(G)

bundles = [[1], [3], [2]]
G = envy_graph(agents, bundles)
print_envy_graph(G)

bundles = [[2], [1], [3]]
G = envy_graph(agents, bundles)
print_envy_graph(G)
