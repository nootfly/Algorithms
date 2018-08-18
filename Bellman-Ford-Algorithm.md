# Bellman Ford Algorithm

>The Bellman–Ford algorithm is an algorithm that computes shortest paths from a single source vertex to all of the other vertices in a weighted digraph. It is slower than Dijkstra's algorithm for the same problem, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers.

> Note that if a graph contains a “negative cycle” (i.e. a cycle whose edges sum to a negative value) that is reachable from the source, then there is no shortest path. Any path that has a point on the negative cycle can be made cheaper by one more walk around the negative cycle. Bellman–Ford algorithm can easily detect any negative cycles in the graph.

> The algorithm initializes the distance to the source to 0 and all other nodes to infinity. Then for all edges, if the distance to the destination can be shortened by taking the edge, the distance is updated to the new lower value. At each iteration i that the edges are scanned, the algorithm finds all shortest paths of at most length i edges. Since the longest possible path without a cycle can be V-1 edges, the edges must be scanned V-1 times to ensure the shortest path has been found for all nodes. A final scan of all the edges is performed and if any distance is updated, then a path of length |V| edges has been found which can only occur if at least one negative cycle exists in the graph.

## Time Complexity

O(|V| * |E|), where |V| and |E| are the number of vertices and edges respectively


## Code

   ```python
  def print_path(parent, i):
    if i < 0:
        return
    print_path(parent, parent[i])
    print(str(i), end= ' ')
     
  def bellmanford(g, V, source):
    distances = [sys.maxsize for _ in range(V)]
    parent = [None for _ in range(V)]
    parent[source] = -1
    distances[source] = 0

    for _ in range(V - 1): 
      for i in range(V):
        for j in g.edges(i):
           dest = j.dest
           source = j.source
           weight = j.weight
        
           if distances[source] + weight < distances[dest]:
                distances[dest] = distances[source] + weight
                parent[dest] = source 
           
    for i in range(V):
        for j in g.edges(i):
           dest = j.dest
           source = j.source
           weight = j.weight
        
           if distances[source] + weight < distances[dest]:
                return True
    
    for i in range(V):
        print("Distance of vertex " + str(i) + " from the source is " + str(distances[i]) + ". It's path is \n[", end="")
        print_path(parent, i)
        print("]")
    
    return False
   ```

References:

[Single-Source Shortest Paths – Bellman Ford Algorithm](http://www.techiedelight.com/single-source-shortest-paths-bellman-ford-algorithm/)

[https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
