# Nash-Equilibrium
  
In game theory, the Nash equilibrium is a set of strategies where for each player where the following property holds: given each other players' strategies are constant, no player can deviate their strategy for a higher average payout.  
  
This program can compute pure and mixed strategy Nash equilibra. In pure strategy, each player plays only one move. In mixed strategy, each player can play multiple moves with different probabilities.  

To run the program, provide an input file as the first argument and a choice of strategy as the second argument. E.g.

    python nash_eq.py file.txt -p  

`-p` prints the pure strategy Nash equilibriums  
`-m` prints the mixed strategy Nash equilibriums 

Input files have the following format:  
  
    1,1 1,2 1,3  
    2,1 2,2 2,3  
    3,1 3,2 3,3  
  
Rows represent player 1's moves while columns represent player 2's moves. Each (row, column) pair represents an outcome from a combination of the two players' moves. The first value is player 1's payout, the second value is player 2's payout. 
  
This program requires numpy.