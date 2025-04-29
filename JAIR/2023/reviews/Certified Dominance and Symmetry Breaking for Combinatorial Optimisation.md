
## Certified Dominance and Symmetry Breaking for Combinatorial Optimisation
Bart Bogaerts, Stephan Gocht, Ciaran McCreesh, Jakob Nordström
Keywords: 
JAIR/2023/Proceedings/14296 - Certified Dominance and Symmetry Breaking for Combinatorial Optimisation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide an implementation in the references (https://zenodo.org/records/6373986). The authors state some notes regarding the implementation in section 5. In the readme they overview the directories and files in the folder. The solvers in the tools directory have their own readmes. There is installation instructions in the readme for the crystal maze-solver. Very few comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

There is a download script in the implementation regarding SAT competition bechmarks. The authors us a subset of this benchmark and describe the selection process in 4.4. More details would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

No parameters used/discussed.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors mesure time in seconds and the proofsize in mega/gigabytes on a sliding color scale. They also show out of memory (16 Gbytes) and timeouts (5000/100,000 seconds)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on SAT solving.
