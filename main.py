from src.fiber_network import minimum_cable_length
from src.visualize import draw_full_graph, draw_mst_graph

FILE_PATH = "communication_wells.csv"

if __name__ == "__main__":
    result = minimum_cable_length(FILE_PATH)
    print("Мінімальна довжина кабелю:", result)

    draw_full_graph(FILE_PATH)
    draw_mst_graph(FILE_PATH)
