
## Effectiveness of Tree-based Ensembles for Anomaly Discovery: Insights, Batch and Streaming Active Learning
Shubhomoy Das, Md Rakibul Islam, Nitthilan Kannappan Jayakodi, Janardhan Rao Doppa
Keywords: 
JAIR/2024/Proceedings/14741 - Effectiveness of Tree-based Ensembles for Anomaly Discovery: Insights, Batch and Streaming Active Learning.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the introduction in footnote 1 (https://github.com/shubhomoydas/ad_examples). The authors state in the readme how to install the required libraries, how to run the demo, citations to other works used, a list of many examples and techniques, how to execute the code and many demonstrations with output examples. The code has okay comments. An index on the structure is welcome. Pseudo code stated in algorithm 1-8. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(10/10)

The authors use ten benchmark datasets and provide citations in section 7. Their details are listed in table 2. All datasets are available in the implementation. Text descriptions regarding the data is missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors do a parameter sensitivity analysis in 7.2.2. A hyperparameter for algorithm 3 is stated (τ) but not noted afterwards. An overview over the hyperparameter values is not given, they are stated in text. Acquisition not always clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate each experiment 10 times and present averages + 95% CI. The metric is percentage of anomalies selected.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on anomaly discovery.
