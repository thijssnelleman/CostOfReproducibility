## Iterative Train Scheduling under Disruption with Maximum Satisfiability
Alexandre Lemos, Filipe Gouveia, Pedro T. Monteiro, Inês Lynce
Keywords: 
JAIR/2024/Proceedings/14924 - Iterative Train Scheduling under Disruption with Maximum Satisfiability.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors present their implementation online https://github.com/ADDALemos/train-schedule-optimisation. There is a read-me with informations about how to run the code. However, I don't find the file I should run and it is very short and I did not find much about installation, requirements, examples. That is why I increased the costs by 1. I think the main file is main.cc. I don't know the programming language but I do not see many comments. That is why I am increasing the costs by 1. I think the repository structure is difficult to navigate, because of unclear directory/file names. (+1)

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

They evaluate on two data sets and both are available. They post a github repo, that contains both. I think they fulfill all the criteriat. That is why I keep the costs at 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

I think the only hyperparameters you would care about in this context are the ones of the sat solver. They state that they use the default configuration (I do not know if the default configurations are known in the community). I increase the costs by 1 for not referring to a source or summarizing them. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

They are reporting the running time in seconds and number of iterations. Furthermore, they compare encoding size in terms of nodes and edges. I do not know the standard evaluation metrics in the SAT community. However, just measuring seconds seems to me not so easily reproducible. That is why I am increasing the costs by 1. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

I think you would need to do a lot of reading to get the expertise to reproduce this paper. The content contains a lot of non-trivial math, logic and proofs. Additionally, I think you need to have a good knowledge about SAT. That is whay I would set the costs to 7.
