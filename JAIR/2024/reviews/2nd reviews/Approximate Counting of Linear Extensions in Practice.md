## Approximate Counting of Linear Extensions in Practice
Topi Talvitie, Mikko Koivisto
Keywords: 
JAIR/2024/Proceedings/16374 - Approximate Counting of Linear Extensions in Practice.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide their C++ code in a Github repository. To run their code, one must compile it with GCC (or Clang) and the given makefile.  
Further C++ libraries must be installed to successfully compile. Further compilation instructions are provided for GPU-related code that may be specific to one's GPU setup.
Once compiled, the program is available and parameterisable with a CLI.
The code in the `/src/` directory is not further subdivided, causing this directory to be difficult to navigate (+1).
Compilation and the requirement of additional C++ libraries causes further effort and possible sources of errors (+1).
The code lacks comments, however it is meant to be compiled, rather than used directly and the paper contains various "implementation" sections that serve as documentation for their code, as well as pseudocode examples (mitigating factors) (+1).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

Three types of instances are generated through python scripts provided by the authors on Github. These scripts do contain some comments, unlike the C++ implementation files.
Their documentation suggests to use the provided makefile which, in turn, calls the data generation python scripts.
There are no pre-compiled instances, meaning that if there are some errors during generation, there is no fallback (+1).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

Algorithm parameters are hardcoded, and the only exposed parameters are those of the problem instances. These parameters are all provided in the experiments section. Given the guidelines configurations point 3 regarding acquisition on second bullet point, +1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors compare empirical running times of various algorithms. While these results may vary depending on one's architecture (e.g. more/less powerful CPU/GPU), the authors do provide the hardware specifications on which the experiments were carried out.  
All algorithm parameters needed for the CLI are given in the figures.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

The background and methods of this paper are by nature highly theoretical. Getting a grasp of the many mathematical formulations used in the paper would take a significant amount of time. Further, the authors describe many small improvements and code-specific details which, while nicely documented, would add additional effort to re-implement.
