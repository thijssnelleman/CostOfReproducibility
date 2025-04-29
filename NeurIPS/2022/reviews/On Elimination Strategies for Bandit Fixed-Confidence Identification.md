
## On Elimination Strategies for Bandit Fixed-Confidence Identification
Andrea Tirinzoni, Rémy Degenne
Keywords: 
NeurIPS/2022/Proceedings/53572 - On Elimination Strategies for Bandit Fixed-Confidence Identification.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors link their implementation in footnote 6 (https://github.com/AndreaTirinzoni/bandit-elimination). In the readme they state installation requriements, an index on the code files, a table of implemented algorithms and their properties, an explanation on which script to run to reproduce the experiments and some details on running it. The code has good comments. Structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use two bandit structures and for each they consider 3 pure exploration problems (simulators). The simulators seem to be included in the implementation. The parameters are given in sec 4. and appendiux G. They are not explained in great detail. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The parameters specified are all regarding the problem not the algorithm. The method is seemingly parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The results are averaged over 100 runs and variation is standard deviations. The authors measure activate arms and ratio of stoppiong times (problem specific). Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on bandits.
