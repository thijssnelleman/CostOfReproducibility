
## Iterative Train Scheduling under Disruption with Maximum Satisfiability
Alexandre Lemos, Filipe Gouveia, Pedro T. Monteiro, Inês Lynce
Keywords: 
JAIR/2024/Proceedings/14924 - Iterative Train Scheduling under Disruption with Maximum Satisfiability.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the introduction (https://github.com/ADDALemos/train-schedule-optimisation). In the readme they state how to compile the code, but not under which conditions (compiler etc.). They also state a few more dependencies, how to run the code and a list of solvers as well as links to two benchmarks dataset. It is marked in each code file which was written by the authors so its easy to distinguish from lend code (they use multiple solvers from other works). Code has okay comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors describe the problem they aim to solve in the introduction and the datasets they use, as well as section 3. The datasets are cited and characteristics are in table 3.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state they could try parameter tuning in the future. They state they use the solvers with their default configurations. It is not directly clear what these parameters and their value are, but can be extracted from the code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the solvers on the problem with running time in seconds, with a time limit of 900 seconds. They also measure the number of iterations and optimal cost in terms of delay (formula given) and memory used in gigabytes.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on maxsat (solvers) and transforming the original problem to maxsat but it is all well documented.
