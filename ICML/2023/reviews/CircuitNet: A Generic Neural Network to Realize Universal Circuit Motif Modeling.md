
## CircuitNet: A Generic Neural Network to Realize Universal Circuit Motif Modeling
Yansen Wang, XINYANG JIANG, Kan Ren, Caihua Shan, Xufang Luo, Dongqi Han, Kaitao Song, Yifei Shen, Dongsheng Li
Keywords: 
ICML/2023/Proceedings/25018 - CircuitNet: A Generic Neural Network to Realize Universal Circuit Motif Modeling.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not share their implementation. In figure 2 they layout the architecture.  

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(11/11)

The authors conduct synthetic experiments for which they detail the functions in appendix A.1. but do not release the code, three public environments which they cite and provide details on the paramters in table 7 of appendix A, and four benchmark image classification datasets for which they also provide citations. No direct links are present to the data used. The environments are not described, the image tasks are described in a.3. The time series data sets are briefly described in appendix a.4. with citations.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors details their models and parameter choices per task in appendix B. They search various hyperparameter values on grids others are just gvien. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

For the synthetic data set train/test set split is specified in A.1 and use RRSE as a metric. For the environments the authors present training curves of models with average environment return as a metric but the aggregation/variation is not explained. For the image classification they report the accuracy over the static test set (A.3.). For the time series each experiment is repeated three times and they report the average on the test set but the data split is unclear.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on ANNs and their limitations regarding ciruit motifs.
