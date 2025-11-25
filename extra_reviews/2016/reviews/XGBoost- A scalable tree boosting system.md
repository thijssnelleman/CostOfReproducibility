## XGBoost- A scalable tree boosting system
Tianqi Chen, Carlos Guestrin
Keywords: Large-scale Machine Learning
extra_reviews/2016/Proceedings/XGBoost- A scalable tree boosting system.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in footnote 2 of the introduction (https://github.com/dmlc/xgboost). The package is extremely well documented with its own documentation website.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use Allstate, Higgs Boson, Yahoo LTRC and Criteo benchmark datasets and provide a summary in table 2. Links provided for each. Descriptions are relatively short.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors evaluate the method with various parameter settings, parameters are defined in algorithm 1-3. Values per experiment defined, but a structured overview is missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure Test set AUC over iterations, time per tree in seconds (over number of threads or number of training examples), and time per iteration over number of machines. The authors use the official train test splits. Results are single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
