import networkx as nx
import matplotlib.pyplot as plt
from src.fiber_network import read_edges_from_csv, compute_mst


def draw_full_graph(file_path):
    edges, _ = read_edges_from_csv(file_path)
    G = nx.Graph()
    for weight, u, v in edges:
        G.add_edge(u, v, weight=weight)

    _draw_graph(G, title="Повний граф колодязів")


def draw_mst_graph(file_path):
    mst_edges = compute_mst(file_path)
    if mst_edges is None:
        print("⚠️ MST не існує (граф не зв'язний)")
        return

    G = nx.Graph()
    for u, v, weight in mst_edges:
        G.add_edge(u, v, weight=weight)

    _draw_graph(G, title="Мінімальне остовне дерево (MST)")


def _draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)
    edge_labels = nx.get_edge_attributes(G, "weight")

    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
