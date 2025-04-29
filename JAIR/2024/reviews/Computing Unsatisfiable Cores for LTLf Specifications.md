
## Computing Unsatisfiable Cores for LTLf Specifications
Marco Roveri, Claudio Di Ciccio, Chiara Di Francescomarino, Chiara Ghidini
Keywords: 
JAIR/2024/Proceedings/15313 - Computing Unsatisfiable Cores for LTLf Specifications.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors share 6 implementation links for algorithms used in their experiments. The authors extend existing implementations for their application. The main repository seems to be linked in 5.2 ( https://github.com/roveri-marco/ltlfuc/archive/refs/tags/jair-release-v1.0.zip). The readme is pretty empty, there are few comments, no index, no installation instructions and its not specified exactly what they modified.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors state the benchmarks used in their experiments in table 2 with statistics. Its not clear if they are available in the implementation (chaotic repo). Citation is provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The methods seem to be parameter free based on the pseudo code (no parameters discussed).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate cumulative CPU time in seconds over solved instances. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on SAT solving.
