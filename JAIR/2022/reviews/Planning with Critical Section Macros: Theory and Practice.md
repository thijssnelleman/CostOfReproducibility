
## Planning with Critical Section Macros: Theory and Practice
Lukas Chrpa, Mauro Vallati
Keywords: 
JAIR/2022/Proceedings/13269 - Planning with Critical Section Macros: Theory and Practice.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in 7.4. footnote 5 (https://github.com/lchrpa/CSMs). In the readme they state a structure overview of the files/directories, how to compile but not under which conditions, how to run the code, explanation on the parameters and contact details. Code can use more comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(15/15)

The authors state the benchmarks used in 7.1 and provide the files for each in the implementation. No description on the problems.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the values ov v1 and v2 according to the results of preliminary experiments and provide the values in 7.3. There is no structured overview. Budget for acquisition unclear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use Coverage (number of solved problems), PAR10 and IPC as metrics and explain them in 7.2. The results are presented as average over the instances. They also visualise per domain how many planners were able to solve instances. They state in 7.2 they present the results on testing task with a time limit of 900s and memory limit of 4 gb.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on planning.
