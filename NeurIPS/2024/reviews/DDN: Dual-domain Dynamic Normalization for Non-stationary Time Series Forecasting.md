
## DDN: Dual-domain Dynamic Normalization for Non-stationary Time Series Forecasting
Tao Dai, Beiliang Wu, Peiyuan Liu, Naiqi Li, Xue Yuerong, Shu-Tao Xia, Zexuan Zhu
Keywords: 
NeurIPS/2024/Proceedings/95167 - DDN: Dual-domain Dynamic Normalization for Non-stationary Time Series Forecasting.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/Hank0626/DDN). In the readme they state an introduction to the method and the results, how to install, a link to the datasets, how to run the code and acknowledgements to other implementations they build upon. The code has some comments but a substantial amount are cryptic. The repository has quite some files and directories and for the scripts the depth is quite deep but they do provide a readme per dir in the scripts dir. Overview of the method given in figure 2 and 3.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(7/7)

The authors discuss the datasets in sec 4 with a citation, explain each one with statistics in A.1. and table 6, and provide a direct links to them. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

In appendix A.2. the authors discuss the settings of the method. For many values they refer to a previous work. The full parameters used per experiment are available in the implementation scripts directory. No acquisition specified for all parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics are stated in sec 4 which are both standard. The authors state they repeated the experiment three times with consistent random seeds and they present the mean (no variation). The data set split is clearly specified in A.1 per dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on time series data and DNN normailzation.
