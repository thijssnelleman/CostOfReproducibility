
## FlexiBERT: Are Current Transformer Architectures too Homogeneous and Rigid?
Shikhar Tuli, Bhishma Dedhia, Shreshth Tuli, Niraj K. Jha
Keywords: 
JAIR/2023/Proceedings/13942 - FlexiBERT: Are Current Transformer Architectures too Homogeneous and Rigid?.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The implementation is provided in footnote 2 (https://github.com/jha-lab/txf_design-space). In the readme they state a table of contents, how to install, how to replicate the results, and some acknowledgements. Code has good comments. Structure is quite large and can use an index. Overview given in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use datasets from the GLUE benchmark (citation provided). Its unclear if the links are provided in the code. No description or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state motivation for a neural architecture search in 2.2 and that they use GOBI (Citation provided). Hyperparameters are stated in table 7 per task/data set in the benchmark. They state its the 'best hyperparameters' and were selected using auto-tuning technique and the ranges over which they are selected.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors use as metrics: the GLUE score (not explained), number of parameters, Matthews and spearman correlation, F1-score and accuracy. The results are plotted with 90% CI over 50 runs. Data split not clear or what is being evaluated on. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on NLP and NAS.
