## ContraNorm: A Contrastive Learning Perspective on Oversmoothing and Beyond
Xiaojun Guo, Yifei Wang, Tianqi Du, Yisen Wang
Keywords: 
ICLR/2023/Proceedings/11036 - ContraNorm: A Contrastive Learning Perspective on Oversmoothing and Beyond.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

Authors provide a link to their implementation in the abstract (https://github.com/PKU-ML/ContraNorm). Readme contains detailed file structure, and readme per subdirectory in which code examples are given. Some installation instructions are present but complete overview is missing. Code can use more comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

Authors use GLUE, ImageNet1K, Cora, Citeseer and citations are provided for all. A few more details are given in appendix G/H. Most are present in the implementation. Detailed descriptions are missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors plug their method into existing models and select the best value of their HP s over a grid. A motivation is provided in appendix E. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

The authors measure matthews correlation, variance, effective rank, test accuracy over single runs. Data set split specified in 4.3. Results are averaged over 5 runs, variation unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
