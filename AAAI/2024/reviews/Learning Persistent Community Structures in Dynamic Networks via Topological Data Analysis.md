
## Learning Persistent Community Structures in Dynamic Networks via Topological Data Analysis
Dexu  Kong, Anping Zhang, Yang Li
Keywords: DMKM: Graph Mining, Social Network Analysis & Community, ML: Clustering, ML: Deep Learning Algorithms
AAAI/2024/Proceedings/29366 - Learning Persistent Community Structures in Dynamic Networks via Topological Data Analysis.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a github repository (https://github.com/kundtx/MFC-TopoReg) with a short documentation on how to run the code, including a demo notebook. The code has some comments too but could do with more extensive explanation. The authors provide visualisations and examples in their paper.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The data is publicly available, cited, and posted in their implementation repository including data loaders. The authors provide multiple pseudo code examples.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors provide us with a few hyper parameters in their experimental settings subsection, but not all seem present there. In their implementation there is an "args dict" going into each model, but it is not completely made clear what values it can contain and what is being fed into it. There is no explanation on how the given values were acquired. Semantic parameters are noted.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[7]

The metrics used are explained, but exactly how the results were acquired (e.g. how many times the process was run, train and test set details..)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method is well documented and is relatively accessible, in part due to the many examples provided.
