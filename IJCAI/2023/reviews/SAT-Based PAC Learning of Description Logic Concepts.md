
## SAT-Based PAC Learning of Description Logic Concepts
Balder ten Cate, Maurice Funk, Jean Christoph Jung, Carsten Lutz
Keywords: Knowledge Representation and Reasoning: KRR: Description logics and ontologies, Knowledge Representation and Reasoning: KRR: Learning and reasoning
Award: Distinguished Paper
IJCAI/2023/Proceedings/0373 - SAT-Based PAC Learning of Description Logic Concepts.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/spell-system/SPELL). In the readme they state how to install the implementation and verify that its correct, how to run an example and how to get more information on the arguments of the implementation. They also give a demo for visualisation. They also give a readme on how to reproduce the results from the paper with exact commands. The code has very few comments however, making it difficult to follow the process for re-implementation. Otherwise the documentation is outstanding.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors share the benchmarks on github. They state existing benchmarks do not suit their purpose and therefore provide their own, which they designed. However, no details are given on how this was designed, any descriptions or statistics. This will have to be extracted from the shared data in order to defend comparability or determine acquisition costs. However there are generation scripts present in the implementation which could be useful.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method is seemingly parameter free based on the implementation and experiment descriptions. The parameters they explore in figure 1 are regarding the data.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors conduct running time experiments on the method in experiment. It is seemingly straightforward, however due to the complexity of the method/problem this will take some expertise/time to fully understand.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise in sat solving, the task (reasoning/ logic description).
