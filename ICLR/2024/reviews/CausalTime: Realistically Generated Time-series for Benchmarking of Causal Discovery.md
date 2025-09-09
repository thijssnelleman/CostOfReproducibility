## CausalTime: Realistically Generated Time-series for Benchmarking of Causal Discovery
YUXIAO CHENG, Ziqian Wang, Tingxiong Xiao, Qin Zhong, Jinli Suo, Kunlun He
Keywords: 
ICLR/2024/Proceedings/18059 - CausalTime: Realistically Generated Time-series for Benchmarking of Causal Discovery.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors link their implementation in the reproducibility statement (https://github.com/jarrycyx/UNN). In the readme they state a table with previous research papers and other code links used. They also state which subdir contains the code of the paper. In the readme they state how to install (albeit with a typo in the file) and how to run the demo. The code has few comments and there are no real examples on how to run except for the demo which is not very detailed.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors provide a link for the generated CausalTime dataset in the reproducibility statement. There is also generation code available although not clearly stated how this was used for the dataset, although the demo should help. Statistics provided in 4.1. Furthermore authors use AQI, Traffic and Medical, all cited and explained in A.2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

HP values discussed in appendix A.2. and table 4, the best values per baseline were searched using the validation set. Values summarised in table 4/5 of appendix A.2.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Authors measure Discriminative Score, MMD (both explained) AUROC and AUPRC (standard). The variation/aggregation of table 2 is not clear. Table 3 contains results over 5 random seeds but agg/var not given. results on test set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
