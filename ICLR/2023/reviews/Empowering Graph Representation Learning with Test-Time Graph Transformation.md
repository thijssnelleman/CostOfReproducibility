## Empowering Graph Representation Learning with Test-Time Graph Transformation
Wei Jin, Tong Zhao, Jiayuan Ding, Yozen Liu, Jiliang Tang, Neil Shah
Keywords: 
ICLR/2023/Proceedings/10910 - Empowering Graph Representation Learning with Test-Time Graph Transformation.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/ChandlerBang/GTrans). In the readme they provide installation instructions, a link to download all datasets and how to place them into the code, how to run the code with various parameter settings and some explanation. Code has few comments and no index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The authors use CORA, Amazon-Photo, Twitch-E and FB-100, Eliptic, OGB-Arxiv (All have citations, details and statistics in appendix C), data link in implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HP values are given per experiment in appendix C, in text. Structured overview and acquisition missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Experiments are repeated with 10 different seeds, data splits given in section 4.1. Results are on test set presented with average but variation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
