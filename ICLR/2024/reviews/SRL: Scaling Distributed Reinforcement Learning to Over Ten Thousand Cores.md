## SRL: Scaling Distributed Reinforcement Learning to Over Ten Thousand Cores
Zhiyu Mei, Wei Fu, Jiaxuan Gao, Guangju Wang, Huanchen Zhang, Yi Wu
Keywords: 
ICLR/2024/Proceedings/17927 - SRL: Scaling Distributed Reinforcement Learning to Over Ten Thousand Cores.pdf
Project URL: https://github.com/openpsi-project/srl

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

Authors provide a link to the implementation in the abstract (https://github.com/openpsi-project/srl). Readme contains details on the implementation including directory overview, how to setup/install, example on how to run. Code needs more comments, structure overview needs to be more detailed due to size of the project.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

Atari, gFootball, StarCraft Multi-Agent Challenge, DMLab, all cited. Installs with the code. No descriptions.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HP values per experiment summarised in table 12 of appendix D. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Authors measure FPS over num CPU cores, IQM (cited, not explained). Presented with avereaged + 95CI over 5 seeds. Split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
