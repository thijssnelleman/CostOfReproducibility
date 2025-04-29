
## Engineering an Efficient Approximate DNF-Counter
Mate Soos, Divesh Aggarwal, Sourav Chakraborty, Kuldeep S. Meel, Maciej Obremski
Keywords: Constraint Satisfaction and Optimization: CSO: Solvers and tools
IJCAI/2023/Proceedings/0226 - Engineering an Efficient Approximate DNF-Counter.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/meelgroup/pepin). In the readme, there is a brief instruction on the input, how to build/run, and known limitations. They also show how their implementation can be used a s a library. The code seems to have a decent amount of comments/documentation. In the paper the authors provide pseudo code on their method in algorithm 1,2,3 and 4. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors state they use a benchmark generation tool and cite a previous work. They also state the ranges for the generation. However full details on this generator would have to be determined by following the citation. There is a random dnf generator present in the scripts of the implementation, and its indiciated this is the implementation meant for generation but requires some verification. The originally generated files are not presented.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

Several parameter values are stated in section 5, but it is unclear whether all belong to the benchmark generation or also to the methods as they are stated in section 2 as parameters. Requires expertise in the subdomain and with the previous work.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the timeout of their experiments and the metric used (and explain it in footnote 3). In table 1 it implicitly shows how many problems were evaluated. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires both theoretical and applied experience with the domain as many things are left obscured.
