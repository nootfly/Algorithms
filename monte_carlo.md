*  [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method)

    >Monte Carlo methods vary, but tend to follow a particular pattern:

    >Define a domain of possible inputs
Generate inputs randomly from a probability distribution over the domain
Perform a deterministic computation on the inputs
Aggregate the results

* [What is Monte Carlo Simulation](https://www.riskamp.com/files/RiskAMP%20-%20Monte%20Carlo%20Simulation.pdf)

  >Monte Carlo simulation, or probability simulation, is a technique used to understand the impact of risk and uncertainty in financial, project management, cost, and other forecasting models.

  >In a Monte Carlo simulation, a random value is selected for each of the tasks, based on the range of estimates. The model is calculated based on this random value. The result of the model is recorded, and the process is repeated. A typical Monte Carlo simulation calculates the model hundreds or thousands of times, each time using different randomly-selected values.
When the simulation is complete, we have a large number of results from the model, each based on random input values. These results are used to describe the likelihood, or probability, of reaching various results in the model.

* [Calculation of Pi Using the Monte Carlo Method](http://www.eveandersson.com/pi/monte-carlo-circle)

  >If a circle of radius R is inscribed inside a square with side length 2R, then the area of the circle will be pi*R^2 and the area of the square will be (2R)^2. So the ratio of the area of the circle to the area of the square will be pi/4.

  >This means that, if you pick N points at random inside the square, approximately N*pi/4 of those points should fall inside the circle.

  >This program picks points at random inside the square. It then checks to see if the point is inside the circle (it knows it's inside the circle if x^2 + y^2 < R^2, where x and y are the coordinates of the point and R is the radius of the circle). The program keeps track of how many points it's picked so far (N) and how many of those points fell inside the circle (M).

   > Pi is then approximated as follows:

           4*M
      pi = ---
            N

