# Search-Algorithms
-Displays the Greedy Best First Search and A-Star Search Algorithms

-When given a graph representing all 48 contiguous US states and asked what the most efficent route is between two states its clear to see how a search algorithm can efficently answer this question.  

-We are provided two csv files containing straightline distances between two states and driving distances between neighboring states for all 48 states. 

-The straightline distances are used as a heurisitic in both search algorithms but for Greedy Best First Search it only relies on the node heuristic when expanding nodes.  

-For A-Star algorithm, it relies on adding the node heuristic to the distance needed to travel when expanding the node. Obviously the lowest cost of h(n)+g(n) will deterimine the next node to travel to.  

*When running the python script provide two state(Ex. WA TX) inputs representing the initial state and goal state. What is returned is the conclusion made by both algorithms stating path cost, solution path, and execution time.

![Capture1](https://user-images.githubusercontent.com/89810188/232182089-519ea70e-5393-4475-8dfe-b14235e68f46.PNG)


![Capture](https://user-images.githubusercontent.com/89810188/232182047-3e48a134-e7ca-468f-9ce5-c9011d1ce3d5.PNG)


