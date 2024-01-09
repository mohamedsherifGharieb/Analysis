from collections import defaultdict, deque
import collections

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def Addedge(self, u, v):
        self.adj_list[u].append(v)

    def depthfirstsearch(self, start):
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                print(node, end=' ')
                stack.extend(sorted(self.adj_list[node], reverse=True))


    def breadthfirstsearch(self, root):  
        visited, queue = set(), collections.deque([root])
        visited.add(root)

        while queue:
            vertex = queue.popleft()
            print(str(vertex) + " ", end="")

            for neighbour in self.adj_list[vertex]:  # Updated to use 'self.adj_list'
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)


    def cyclesSearch(self, start):
        visited = set()
        stack = [(start, [])]

        while stack:
            node, path = stack.pop()
            if node in path:
                cycle_start = path.index(node)
                cycle = path[cycle_start:] + [node]
                print('Cycle:', ' '.join(map(str, cycle)))
                continue

            visited.add(node)
            for neighbor in self.adj_list[node]:
                stack.append((neighbor, path + [node]))

    def bipartite(self, start):
        colors = {}
        queue = deque([start])
        colors[start] = 1

        while queue:
            node = queue.popleft()
            for neighbor in self.adj_list[node]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True

if __name__ == "__main__":
    graph = Graph()
    edges = [(1, 3), (1, 4), (2, 1), (2, 3), (3, 4), (4, 1), (4, 2)]
    for u, v in edges:
        graph.Addedge(u, v)

    print("DFS :")
    graph.depthfirstsearch(1)
    print("\nBFS :")
    graph.breadthfirstsearch(1)
    print("\nCycles:")
    graph.cyclesSearch(1)

    bipartite = graph.bipartite(1)
    print("bipartite?", "Sha8al" if bipartite else "LAAAAAA3")
