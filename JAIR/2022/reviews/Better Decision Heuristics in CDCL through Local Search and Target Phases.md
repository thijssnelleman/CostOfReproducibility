
## Better Decision Heuristics in CDCL through Local Search and Target Phases
Shaowei Cai, Xindi Zhang, Mathias Fleury, Armin Biere
Keywords: 
JAIR/2022/Proceedings/13666 - Better Decision Heuristics in CDCL through Local Search and Target Phases.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in footnote 2 (http://lcs.ios.ac.cn/~caisw/Code/JAIR-SATcodes.zip). The authors use implementations of other works for their work, and include each with a readme and installation notes. They also include some command line notes for them in the zip file. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

The authors evaluate on the SAT competitions and SAT Race over the last three years (No links/citations), as well as an application benchmark suite (Linked and cited) and the FCC dataset (cited and linked.)

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors describe the configurations they test in 7.1.2. They are also available in the implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure runtime and use penalised runtime average (PAR2) as metric (explained). Theey also measure SAT/UNSAT (problem specific) and number of problems solved. The y-axis in the figures is not defined. The cutoff is 5000 seconds.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on SAT.
