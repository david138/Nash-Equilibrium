# Nash-Equilibrium

The Nash Equilibrium is a set of strategies for each player with the following property: given each other players strategies are constant, no player can deviate their strategy for a higher average payout.

This program can compute pure and mixed strategy nash equilibriums.
Pure strategy means each player plays only one move.
Mixed strategy means each player can play multiple moves with different probabilities.

The input files have the following format:

1,1 1,2 1,3
2,1 2,2 2,3
3,1 3,2 3,3

Each row is a move player 1 can perform and each column is a move player 2 can perform.
There is a cell for each row for each column that represents player 1 playing that row and player 2 playing that column.
Each cell has player 1's payout followed by player 2's payout for the given player moves.
