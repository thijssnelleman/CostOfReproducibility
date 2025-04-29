
## Network Regression with Graph Laplacians
Yidong Zhou, Hans-Georg Müller
Keywords: 
JMLR/2022/Proceedings/220681 - Network Regression with Graph Laplacians.pdf
Project URL: https://github.com/yidongzhou/Network-Regression-with-Graph-Laplacians

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state the implementation link on JMLR website as wel as in the implementation details section (https://github.com/yidongzhou/Network-Regression-with-Graph-Laplacians). In the readme they state a summary of the paper, an overview of the files with detailed explanations and how to get the data. The code has okay comments. No installation instructions.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(6/6)

The authors use four simulation scenarios and provide details on them in table 1 and section 5.2. Code is available in 'simulation.R' in the implementation. Section 6.1 uses Yellow Taxi data which is described and a link is provided, they also use the COIVD-19 dataset and also describe it and give extended statistics in figure 7. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state bandwiths for local networks were chosen by leave-one-out cross-validation. Selected value not given for the simulations, for the datasets its stated to result in h = 0.20. How different values were sampled is not stated.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors report integrated square errors (ISE) and mean ISE (MISE) in figure 5 (boxplots) and table 2 over the sample sizes in fig 5 and table 2. For the real datasets the authors use heatmaps to visualise the predictions, metrics are the same and stated the values in the text.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on graph Laplacian.
