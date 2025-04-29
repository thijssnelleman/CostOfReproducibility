
## Parameterized Local Search for Max c-Cut
Jaroslav Garvardt, Niels Grüttemeier, Christian Komusiewicz, Nils Morawietz
Keywords: Search: S: Local search
IJCAI/2023/Proceedings/0620 - Parameterized Local Search for Max c-Cut.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors do not provide their implementation. They do state in section 6 that they implemented it in JAVA/Kotlin with the JGraphT library, and speicifc regarding parts of the algorithm implementation with a citation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors state they use a benchmark dataset with direct link with citations. Some statistics on the data set are given and the data is explained briefly. The task is a well established problem.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The method seems to be parameter free but this is difficult to verify without implementation or pseudo code. There is no mention of parameter values for the experiments. However it is called 'parametrized local search' in the title, so exactly what role this plays into their experiment requires expertise in the subfield to determine.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors run their method on the presented data set and measure how fast their method produces a better solution. This makes it a straightforward experiment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience in search/local search and the problem (max c-CUT).
