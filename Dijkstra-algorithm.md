# Dijkstra’s Algorithm

`Dijkstra's algorithm` is an algorithm for finding the shortest paths between nodes in a graph. It was conceived by computer scientist Edsger W. Dijkstra in 1956 and published three years later. In artificial intelligence, Dijkstra's algorithm or a variant of it is known as `uniform cost search` and formulated as an instance of the more general idea of `best-first search`. From a dynamic programming point of view, `Dijkstra's algorithm` is a successive approximation scheme that solves the `dynamic programming` functional equation for the shortest path problem by the `Reaching` method.

## Problem

Given a source vertex s from set of vertices V in a weighted graph where all its edge weights w(u, v) are non-negative, find the shortest-path weights d(s, v) from given source s for all vertices v present in the graph

## Algorithm

> Dijkstra’s Algorithm is based on the principle of relaxation, in which an approximation to the correct distance is gradually replaced by more accurate values until shortest distance is reached. The approximate distance to each vertex is always an overestimate of the true distance, and is replaced by the minimum of its old value with the length of a newly found path. It uses a priority queue to greedily select the closest vertex that has not yet been processed and performs this relaxation process on all of its outgoing edges.

## Time Complexity

O(|E| + |V|log|V|)

## Code

   ```python
   def dijkstra(g, source, N):
    heap = []
    heappush(heap, (0, source))
    
    dist = [sys.maxsize for _ in range(N)]
    dist[source] = 0
    visited = [False for _ in range(N)]
    visited[source] = True
    parent = [None for _ in range(N)]
    parent[source] = -1
    
    while heap:
       print(heap) 
       weight, u = heappop(heap)
       
       for edge in g.edges(u):
          v = edge.dest
          w = edge.weight
          if visited[v] == False and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                heappush(heap, (dist[v], v))
                
       visited[u] = True
       
         
    for i in range(N):
        print("Path from vertex " + str(source) + " to vertex " + str(i) +
                            " has minimum cost of " + str(dist[i]) + 
                            " and the route is [", end = ' ')
        print_path(parent, i)
        print("]")
    
    
def print_path(parent, i):
    if i < 0:
        return
    print_path(parent, parent[i])
    print(str(i), end=" ")
   ```