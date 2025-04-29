
## SARAD: Spatial Association-Aware Anomaly Detection and Diagnosis for Multivariate Time Series
Zhihao Dai, Ligang He, Shuanghua Yang, Matthew Leeke
Keywords: 
NeurIPS/2024/Proceedings/94119 - SARAD: Spatial Association-Aware Anomaly Detection and Diagnosis for Multivariate Time Series.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their implementation online (https://github.com/daidahao/SARAD/). In the readme they describe the method, provide installation instructions, how to run the code and how to set parameters, and some acknowledgements of other code used for theirs. The repository structure is huge and needs an index. The comments in the code are good although some are chaotic.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors provide direct links to two datasets (SMD and PSM) in the implementation. In section 4.1. the authors state they evaluate on four real-world datasets which they provide citations on. Statistics given in table 2. Extensive descriptions given in appendix E.1. SWaT data set downloads automatically in the code HAI appearantly not but its used version is stated in E.1. at least.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide configuration files in the implementation. In appendix F they state various hyperparameter values and state they tuned this over 80/20 train/validation split using three grids and TPE sampling. Hyperparameter sensitivity is visualised in appendix H. Not all parameters tuning is given. The selected values are not completely clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are stated in sec 4. They are described with citations and . In sec 4.1. the authors also state the datasets contain training and test split as well as table 2. The authors present the results as averaged over five random seeds. (No variation). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on multi variate time series and temporal modeling.
