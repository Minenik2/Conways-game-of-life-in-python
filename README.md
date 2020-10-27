# Conways-game-of-life-in-python
Game of life coded in python, mainly Norweigan

This is a simulation/'zero player game' where the person gives 2 inputs, one for length and other one for width, these inputs makes a table of the same length and width.
In these table are cells, they are either dead or alive. The game starts at generation 0, when generating the first generation all the cells have a 1 in 3 chance (33%) each to be alive. Once it's randomly choosen which cells are alive or not we can move over to the next degeration.
If a cell is alive, it will die if it has less than 2 or more than 3 alive cells as its neighbours. 
(dies in less than 2 because underpopulation, dies in more than 3 because overpopulation)
If a cell is dead, it will live if it has exacly 3 live cells as it's neighbours.
(lives if it's dead and has exacly 3 alive neighbours due to reproduction)
The player can then press enter to move to the next generation, there's a counter that shows the amount of the cells alive at this current generation.
And so the player can continue to advance to next generations to simulate the lives of these randomly spawned cells.
(This makes me question if god didn't just make us to watch how far we can go)
If the player becomes bored or the current seed (randomly spawned cells) satisfy him anymore. The player can press "r" and then enter to restart the game
with newly randomly spawned cells with generation 0 again. Or the player can press "q" and enter to quit the game.

# Programming
The code is split into 3 chunks, celle.py is a class with the cell object, this object has a value of either being dead or alive. Secondly this object also has
an list (array) with all of it's neightbours. How we append the objects to that list is found in spillbrett.py this file has an object for the whole board. 

When the board is made, each time a cell is created it checks where it's posision is on the grid. If the cells is not on the left corner it will make an 
neightbour to left of itself, that neightbour also makes the cell a neibours to its right, being this current cell, so it basically goes back and fourth.
If the cell is not at the top corner it will make a neighbour to it's 3 top neighbours and so will the top 3 neighbours make a neighbour to the current cell.

This is better explained in voice but you guys just have to understand it in text sadly.

I can still show some pictures for better understanding

Now imagine this list is a two dimensional one. Where we have the x axis and Y axis.
The list is not finished but we are assigning the neighbours as we go.
Y[][][][][]
Y[][]
Y = y axis, mostly made so that the arrays won't collapse on itself for these examples

Here we stopped at list[1][1] (1 in y axis and one iN x axis), + = appended neighbours, . = current cell
Y[+][+][+][][]
Y[+][.]
The + indicates the neibours that our current cell will append. For example .append(list[x-1][y-1])
for the top left neighbour.
These cells wil also append the current cell back so we dont have to append the future cell with the current one, because the future cell will do it for us.

And so we itirate true all of this and make expetion when needed, for example if the current cell is on the left corner it will only append top and top right
Y[][][][][]
Y[][][][][]
Y[+][+][][][]
Y[.]

Another exception is when the cell is at the right corner then it will only append top left, top and left neightbours.
Y[][][][][]
Y[][][][][]
Y[][][][+][+]
Y[][][][+][.]

Another exception is if it's at the top of the list then it will only append it's left
Y[][+][.]

And the final exception being that it's the first cell meaning it has no one to append (must feel very lonely for the current cell :C)
Y[.]

That's all for the theory in two dimensional arrays.
