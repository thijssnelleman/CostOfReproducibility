
## UP2ME: Univariate Pre-training to Multivariate Fine-tuning as a General-purpose Framework for Multivariate Time Series Analysis
Yunhao Zhang, Liu Minghao, Shengyang Zhou, Junchi Yan
Keywords: 
ICML/2024/Proceedings/33686 - UP2ME: Univariate Pre-training to Multivariate Fine-tuning as a General-purpose Framework for Multivariate Time Series Analysis.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/Thinklab-SJTU/UP2ME). The authors introduce the method in the readme, provide installation instructions, download links to the data and how to place it in the implementation, and where to find the scripts to run the results from the paper. They als acknowledge other repositories they used to create theirs. The code has a decent amount of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(8/8)

The authors provide a download link to a dataset in their implementation. The authors state in section 3 they use eight real world datasets, which they describe in appendix A.1 with citations and statistics in table 4. Direct links are also provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter values in A.6. per dataset. The authors discuss hyper-parameter r for fine tuning in section 3.2. No other hyperparameter acquisitions are discussed. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Results are averaged over 4 different lengths / missing ratio settings or single run. The metrics used are MSE, MAE and F1 score which are standard. The authors refer in appendix A to a few previous works regarding their train/test splits. It is never actually explicitly stated in the paper that the results are on the test set. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on time series data/tasks.
