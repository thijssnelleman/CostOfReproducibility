
## Streamflow Prediction with Uncertainty Quantification for Water Management: A Constrained Reasoning and Learning Approach
Mohammed Amine Gharsallaoui, Bhupinderjeet Singh, Supriya Savalkar, Aryan Deshwal, Ananth Kalyanaraman, Kirti Rajagopalan, Janardhan Rao Doppa
Keywords: Multidisciplinary Topics and Applications: General, Machine Learning: General
IJCAI/2024/Proceedings/0804 - Streamflow Prediction with Uncertainty Quantification for Water Management: A Constrained Reasoning and Learning Approach.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/aminegha/StreamPred). Here they introduce the method, how to install requirements and how to run the code. The code in general could use more comments. The authors also provide the data sets as pickles. The paper provides pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide the data set files in the implementation documentation. The authors state in 4.1 they collected this data set themselves, on which they provide details. Statistics on the data are provided in table 1. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide configuration details of several baselines with parameter values. However it is difficult to make out if all required values are presented, as there are no summary files given in the implementation documentation. There are no budgets/acquisiton strategies specified, but they do state the validation set was used for hyper-parameter tuning.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used and provide citations on one, the second is standard. The non-standard one is explained in detail. The other two metrics are briefly stated (with description), and are seemingly standard. The authors state they present all results with a single training run. The authors state the t/v/t split on the data. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on spatiotemporal data to understand the task. The method is well documented and the data explained, so any required previous knowledge is not caused by lack of documentation in this case.
