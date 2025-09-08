## NAGphormer: A Tokenized Graph Transformer for Node Classification in Large Graphs
Jinsong Chen, Kaiyuan Gao, Gaichao Li, Kun He
Keywords: 
ICLR/2023/Proceedings/11258 - NAGphormer: A Tokenized Graph Transformer for Node Classification in Large Graphs.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/JHL-HUST/NAGphormer). In the readme they state installation requirements, where to find execution examples and where to download datasets. Code has few comments, and examples offer little explanation.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

Authors use Pubmed CoraFull Computer Photo CS Physics datasets, citations provided and description in appendix D.1 + statistics in table 4. Link in implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP search defined in appendix D.2. Not all values are motivated. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Authors present mean and std dev over 10 random runs with accuracy, datasplits in 4.1. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
