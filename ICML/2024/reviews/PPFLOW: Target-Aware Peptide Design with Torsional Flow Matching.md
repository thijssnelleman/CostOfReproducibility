
## PPFLOW: Target-Aware Peptide Design with Torsional Flow Matching
Haitao Lin, Odin Zhang, Huifeng Zhao, Dejun Jiang, Lirong Wu, Zicheng Liu, Yufei Huang, Stan Z Li
Keywords: 
ICML/2024/Proceedings/34898 - PPFLOW: Target-Aware Peptide Design with Torsional Flow Matching.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/Edapinenut/ppflow). In the readme they state installation instructions, summarise the method, provide details on where to find the processed dataset and how to use it with the code, how train models and infer, and how to evaluate. The code has very few comments. The repository structure is quite simple. The method overview can be seen in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors provide a link to the processed dataset in their implementation. This is their own constructed data set which they detail in 5.1 and appendix B. The authors used a seperate dataset for testing, provide citations and description and minor statistics. The data set is available in the repository. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors method is parametrised with neural networks. The HP values are give in appendix B3. No acquisition method specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used in 5.3 and explain them. The train test split is given in 5.1. The test set is static, thus no aggregation applicable (single model results).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in the cross domain of biomedical research and ML. 
