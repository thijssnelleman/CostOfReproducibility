
## On Tackling Explanation Redundancy in Decision Trees
Yacine Izza, Alexey Ignatiev, Joao Marques-Silva
Keywords: 
JAIR/2022/Proceedings/13575 - On Tackling Explanation Redundancy in Decision Trees.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state a link to their implementation in footnote 19 (https://github.com/izzayacine/xpg) but also an appendix link in footnote 18 (https://github.com/izzayacine/jair22sub/blob/main/TechnicalAnnex/tech-annex.pdf). The package has installation instructions in the readme, as well as how to list options, a description of the input file and examples. Code has good comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(30/30)

The authors use 67 datasets from UCI, PennML and OpenML (citations / links provided) but only provide results for 30 the rest are in the appendix. No details provided on the datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method introduces horn encoding approach and show results with/without this. No other 'parameters' introduced.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors provide runtime in seconds as min/avg/max/total. The authors also measure tree depth, number of nodes, test accuracy and number of paths in the graphs per method. The data split is not clear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on decision trees.
