# ChessPlayer by Arsh Kadakia

This is an autonomous chess player created by me for an assignment in my first-year Algorithms and Data Structures (CSC190) course.

## What it Does:

In summary, it is a chess player that is able to start and finish a game with a reasoned set of calculated moves. This assignment was an extremely important step in my journey as a software developer because it represented my first end-to-end project with defined functions, which determine a reasoning in terms of the reward system (described later). It is unique from other projects because it can be integrated with chess players with the same board convention. These chess players can go against each other.

## How it Does So:

It is in many ways like a regular chess game, where a board convention and point system is defined. A key adaptation is pawns can only move one space at a time. The way that the program is able to make reasoned moves is by the use of the Minimax algorithm and alpha-beta pruning.

The Minimax algorithm chooses the move that will lead to the most optimal evaluation value after a certain value of depth. An example is shown below.

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Minimax.svg/400px-Minimax.svg.png" width="420" height="250"/>

Alpha-beta pruning is useed to eliminate useless paths to save computational power. This allows for the Minimax algorithm to operate on a greater depth of moves.

## Accomplishments:

Key accomplishments from this assignment include:

• Use of trees to fundamentally operate the Minimax Algorithm.

• Use of various Python libraries such as timeit to conduct time analysis for the appropriate depth.

• Creation of evaluation metrics and evaluation algorithms to pick the optimal "next move".

• Creation of a virtual environment in which it is capable to play a chess game.

## Challenges and Things to Work On:

Key challenges that occurred during the work of the project include:

• Making syntactical changes to the potential moves calculations that would reduce computational power of those calculations, so that more power could be used on the Minimax algorithm.

• Accurately determining which depth level would be best for a provided time limit and game state.
