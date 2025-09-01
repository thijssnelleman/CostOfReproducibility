## Bootstrapped Meta-Learning
Sebastian Flennerhag, Yannick Schroecker, Tom Zahavy, Hado van Hasselt, David Silver, Satinder Singh
Keywords: 
Award: Outstanding Paper Award
ICLR/2022/Proceedings/563 - Bootstrapped Meta-Learning.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors do not provide a link to their implementation. They state in appendix C.6. that part of their work is based on the original STACX implementation. The mathematical documentation is extensive. Pseudo code is given in the appendix. 

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(1/2)

The authors use environment to evaluate the method (RL). First they use a tabular grid world for which they give details in 5.1 and document extensively in B.1. but the implementation is not given. Furthermore, the authors use 57 environments from the Atari games collection, citation is provided and link in the appendix, parameters seemingly non applicable (The authors evaluate on all levels of the environment, see appendix C).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

Two color hyperparameters given in table 1, the atari hyper parameters are summarised in table 2 of the appendix. Value selection explained in appendix C.6. although budget is not always clear.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors report the results over three independent runs under different seeds. The authors measure episode return (Environment) and human normalised score (citation provided, not explained). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[9]

-
