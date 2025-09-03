## Learning by Directional Gradient Descent
David Silver, Anirudh Goyal, Ivo Danihelka, Matteo Hessel, Hado van Hasselt
Keywords: 
ICLR/2022/Proceedings/7001 - Learning by Directional Gradient Descent.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[8]

The authors provide code on how to implement DODGE in JAX in listing 1. They also state, with citation, they use JAX in all implementations of their experiment (sec 5) but the implementation is not given.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors use the Copy Problem (synthetic, cited), MNIST (Cited and described), Influence Balancing Task (Cited, described) and Image regression NeRF task (cited, described and reference provided for experimental setup). Direct links not provided. The synthetic tasks seem relatively straightforward. Extensive details missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors state the grids used to choose the best LR in 5.1 and other values there as well. They refer to other works for HP values in A.2. No structured overview given and it is hard to determine if all needed values are there, however as the authors mainly use these HPs of other methods as input to their evaluation this is less important.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors repeat each experiment 5 times with random seeds. They present the training accuracy, and loss with standard error but aggregation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
