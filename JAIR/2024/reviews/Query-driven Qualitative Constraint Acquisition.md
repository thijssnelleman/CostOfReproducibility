
## Query-driven Qualitative Constraint Acquisition
Mohamed-Bachir Belaid, Nassim Belmecheri, Arnaud Gotlieb, Nadjib Lazaar, Helge Spieker
Keywords: 
JAIR/2024/Proceedings/14752 - Query-driven Qualitative Constraint Acquisition.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in section 4 (https://github.com/lirmm/ConstraintAcquisition/tree/GEQCA) and also state another link for an implementation used for their method. Pseudo code available in algorithm 1. In the readme the authors state the executable file and what java environment is needed to run the code. They also state the dependencies for compiling the code. Code needs some more comments, structure is quite large and can use an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors gereate random instances and state the procedure (with citation) in section 4 with the parameter values. Code on it is available with its own readme in the implementation. There are a lot of datasets present, its not clear if their generated one is also there.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors vary the heuristics used in the experiments. The only parameter of GEQCA-II that is not input related is cutoff which is the maximum running time.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measur 'oracle effort' over number of instances and define it in 4.1. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in SAT.
