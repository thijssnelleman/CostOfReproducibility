
## Improving multiple-try Metropolis with local balancing
Philippe Gagnon, Florian Maire, Giacomo Zanella
Keywords: 
JMLR/2023/Proceedings/221351 - Improving multiple-try Metropolis with local balancing.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their Arxiv version of the paper where they post ancillary files containing the implementation (https://arxiv.org/src/2211.11613v2). There is no readme, no installation instructions. Code has okay comments. Structure is actualyl clear because the files/dirs are named after their corresponding sections.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors conduct experiments on a simulation (function) and its defined in 4.3. Parameter values are specified, code for it is in the implementation. In section 5 they use a medical dataset, describe it in 5.1. with details and provide a citation but statistics are lacking, file present in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

There are various mentions of (hyper)parameters but there is no clear statement of what is considered a parameter to their method. In the code the values can be found but it will take a critical eye to understand which is relevant to what.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the method over the defined function in sec 4, metrics of figure 9 not clearly stated. No aggregation or variation applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on bayesian methods, markov chains.
