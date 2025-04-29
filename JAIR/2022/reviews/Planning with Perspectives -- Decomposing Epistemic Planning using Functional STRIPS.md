
## Planning with Perspectives -- Decomposing Epistemic Planning using Functional STRIPS
Guang Hu, Tim Miller, Nir Lipovetzky
Keywords: 
JAIR/2022/Proceedings/13446 - Planning with Perspectives -- Decomposing Epistemic Planning using Functional STRIPS.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in section 5 (https://github.com/guanghuhappysf128/benchmarks). The authors use an implementation from another source in their work and provide a link to it. Their own code file could use some more comments to explain what they did. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors describe the benchmark problems used in section 5.1 and provide citations. The implementation files are included in the implementation. The implementation is quite chaotic however and could use better documentation. Parameters of the problem provided per result. The authors provide the same for Social Media and Gossip, 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors state the options used for a previous work in footnote 1. Other than that no parameters are specified and its not clear if they exist.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results as single runs with a 10-minute time limit. They measure total amount of time in seconds, the compile time  and the time used for external calls. The memory limit is 16 gigabytes.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on planning.
