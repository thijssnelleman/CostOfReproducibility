
## Sample-Level Cross-View Similarity Learning for Incomplete Multi-View Clustering
Suyuan Liu, Junpu Zhang, Yi Wen, Xihong Yang, Siwei Wang, Yi Zhang, En Zhu, Chang Tang, Long Zhao, Xinwang Liu
Keywords: ML: Multi-instance/Multi-view Learning, ML: Clustering
AAAI/2024/Proceedings/30472 - Sample-Level Cross-View Similarity Learning for Incomplete Multi-View Clustering.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a source code repository in their paper (https://github.com/Tracesource/SCSL). However the instructions in the readme only consist of a single line to reproduce the results on the MSRCV dataset. The code sometimes has few comments making it hard to interpret. The data set is also provided in the code, and should run 'out of the box'. The paper has a pseudo code block and various illustrations which lower the cost.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors provide one of the data sets (MSRCV) used in the implementation documentation. The other five datasets are noted as 'widely used' data sets in the paper. The authors provide statistics on all of them. The source of these data sets is unclear and where to find them. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors discuss two parameters and their ranges in the paper. The authors provide an analysis of the impact of these parameter values with an exhaustive grid evaluation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors repeated the experiment 20 times and report mean + std dev for their three metrics. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a high level of understanding of algebra and matrix computations. The provided documentation is well supportive of this, but due to the complexity of the method and room for improvement of the code documentation, this is still quite high.
