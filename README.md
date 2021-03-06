# Automatic Programmer
## Abstract
The aim of the project was to explore the topic of genetic algorithms and automatic programming. In order to do so, we made an application able to solve a CargoBot programming game using genetic algorithm. The game is about moving blocks from initial to final state using simple programming language. We recreated a game with interpreter in our project, so we could use it with genetic algorithm. To evolve grammar and generate programs we used a PonyGE project. As a result of our project we created an automatic programmer, which can play CargoBot game.

## What is it? 
The goal of the project was to write an application, which is able to automatically solve game [Cargo Bot](https://altermanchess.wixsite.com/cargobot). The game is about moving blocks using simple programming language. Our application is using genetic algorithm to generate programs in this language. 
## How it works?
Project was implemented using Python. 
### Game implementation
Game implementation is in a *Game* directory. Part of the code which translates generated programs to game actions is in directory *Game Interpreter*. Interpreter was made using Antlr library. 

Game consists of parts such as:
- Representation of an initial, final and current game board;
- Lift, which moves blocks;
- Program blocks - left arrow, right arrow, down arrow, conditional, subprogram;
- Functions which can execute code commands. 

#### Programs grammar
Game input is a program given as a string in format which is acceptable by game [grammar](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/GameInterpreter/cargobot.g4). Structure of a program consists of parts:
- separator - must occur 3 times, separates 4 subprograms
- left_arrow - move lift by one column to the left
- right_arrow - move lift by one column to the right
- down_arrow - place (if there is a block on a lift) or pick up (if lift is empty) from top of a column where currently is a lift
- program1, program2, program3, program4 - switch execution to subprogram
- color1, color2, color3, color4 - conditional statement meaning if there is a block on a lift in given color (1,2,3 or 4), then do the action; must be followed by action - left_arrow, right_arrow, down_arrow or programX
- all - conditional statement meaning if there is any block on a lift, then do the action; must be followed by action - left_arrow, right_arrow, down_arrow or programX
- empty - conditional statement meaning if lift is empty, then do the action; must be followed by action - left_arrow, right_arrow, down_arrow or programX

#### Execution of a game program
Program is executed using Antlr compiler. 
![alt text](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/ReadmeImages/Execution.PNG "Game program execution")

#### Board structure
For each game execution two game boards are needed - initial state and final state the player wants to achieve. They are stored as json files in directory *GameStates*. There are three fields in the file - initial (*init*) and final state (*end*) and also initial lift position (*liftPosition*). Board state is a two dimensional array written in one line with '|' as a row separator and ',' as a cell seperator.

#### Victory condition
The aim of the game is to think of a program, which is able to transform initial state into final state. 

### Genetic algorithm
Genetic algorithm used to solve this game comes from [PonyGE](https://github.com/PonyGE/PonyGE2) project. It is not a library, so it is not possible to import it. The project was cloned into PonyGE2 directory. 

#### Grammar
There are two types of grammar, which was tested with this algorithm - [full grammar](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/PonyGE2/grammars/cargobot_full.bnf) including conditionals and subprograms, and [simple grammar](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/PonyGE2/grammars/cargobot_simple.bnf) consisting only of one subprogram and arrows. 

#### Fitness function
[Fitness function](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/PonyGE2/src/fitness/cargobot_fitness.py) is a function, which calculates how good generated solution is. If the value is low, it means that the solution is good and should be evolved. High value means that the generated solution is not even close to correct solution. Value 0 is a success - generated program is able to transform initial state into final state. Value is calculated by checking position of each block. If block is on desired position or is close to it, then it means that fitness value is low. Also at the end there should be no block on a lift, so if there is one, then penalty points are added. 

#### Parameters
[Parameters](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/PonyGE2/parameters/cargobot.txt) file contains settings for genetic algorithm. For explanation check [PonyGE documentation](https://github.com/PonyGE/PonyGE2/wiki/Evolutionary-Parameters). Parameters grammar_file, fitness_function and game_board allows to set used grammar, fitness function and file with the board to solve.

### GUI
GUI was made using tkinter. The file consisting GUI code is in a file [gui.py](https://github.com/patrycjabru/AutomaticProgrammer/blob/master/PonyGE2/src/gui.py). GUI is very simple used only for results presentation. It shows 3 boards - initial, final state and achieved by generated program.

## Results
Here are the example results. Simpler boards were better solved by simple grammar. More complicated ones gave better results for full grammar.  
![alt text](https://github.com/patrycjabru/AutomaticProgrammer/raw/master/ReadmeImages/Results1.png "Results 1")
![alt text](https://github.com/patrycjabru/AutomaticProgrammer/raw/master/ReadmeImages/Results2.png "Results 2")

### What is done well?
- Game implementation.
- Input interpreter.
- Genetic program can solve some boards.
- Simple results presentation (GUI).

### What should be improved?
- Genetic program cannot solve some boards.
- Grammar, parameters and fitness function probably can be better. 
- In CargoBot subprograms have fixed length. This constraint was not implemented.
- As a simplification there was removed a possibility of moving a lift out of board. Using left arrow when lift is in a first column, moves a lift to the last column. Analogically for the right arrow at the end.
- GUI could be more complex. There should be more configuration option available. 

## Authors
[@patrycjabru](https://github.com/patrycjabru)
[@hkolanska](https://github.com/hkolanska)
