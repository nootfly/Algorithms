# Travelling salesman problem

> The travelling salesman problem (TSP) asks the following question: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?" It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.

>You can solve TSPs using the Google OR-Tools vehicle routing library, a collection of algorithms designed especially for TSPs, and more general problems with multiple vehicles. The routing library is an added layer on top of the constraint programming solver. See RoutingModel for detailed information about the available methods for setting up and solving routing problems.

>TSP can be solved by Brach and Bound solution.  The worst case complexity of Branch and Bound remains same as that of the Brute Force clearly because in worst case, we may never get a chance to prune a node. Whereas, in practice it performs very well depending on the different instance of the TSP. The complexity also depends on the choice of the bounding function as they are the ones deciding how many nodes to be pruned.





Reference:

[Traveling Salesman Problem](https://developers.google.com/optimization/routing/tsp)

[
The traveling salesman and 10 lines of Python](https://ericphanson.com/posts/2016/the-traveling-salesman-and-10-lines-of-python/)

[Travelling Salesman Problem using Branch and Bound](http://www.techiedelight.com/travelling-salesman-problem-using-branch-and-bound/)

[Branch And Bound](https://www.geeksforgeeks.org/branch-bound-set-5-traveling-salesman-problem/)