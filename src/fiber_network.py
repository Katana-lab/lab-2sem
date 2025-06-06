import csv


class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        self.parent[root2] = root1
        return True


def read_edges_from_csv(file_path):
    edges = []
    nodes = set()
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                continue
            u, v, w = row
            try:
                w = int(w)
                edges.append((w, u, v))
                nodes.update([u, v])
            except ValueError:
                continue
    return edges, nodes


def merge_sort(edges):
    if len(edges) <= 1:
        return edges

    mid = len(edges) // 2
    left = merge_sort(edges[:mid])
    right = merge_sort(edges[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list


def minimum_cable_length(file_path):
    edges, nodes = read_edges_from_csv(file_path)
    edges = merge_sort(edges)
    uf = UnionFind(nodes)
    mst_weight = 0
    edge_count = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst_weight += weight
            edge_count += 1

    if edge_count == len(nodes) - 1:
        return mst_weight
    return -1


def compute_mst(file_path):
    edges, nodes = read_edges_from_csv(file_path)
    edges = merge_sort(edges)
    uf = UnionFind(nodes)
    mst = []

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))

    if len(mst) == len(nodes) - 1:
        return mst
    return None
