
## Conformal Prediction Sets with Limited False Positives
Adam Fisch, Tal Schuster, Tommi Jaakkola, Regina Barzilay
Keywords: 
ICML/2022/Proceedings/17299 - Conformal Prediction Sets with Limited False Positives.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/ajfisch/conformal-fp). In the readme they state how to download the data through a scripts, how to compute set scores, how to train a model, what the seeds in the paper were regarding the experiments, a script to download pretrained models, how to run evaluation and the baselines. Thereare a few notes on the options and the output. The code has alot of comments. Pseudo code is available in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The data automatically downloads through scripts in the implementation. In 5.1 the authors discuss the data sets used with citations. More details are given in appendix C, and statistics are summarised in table 1. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide the seeds of their experiments in the readme. The authors introduce a hyperparameter B in section 4.3. In section 5 tehy state they set it to 100 for all experiments. Ohter parameter details are discussed in appendix C. No acquisition specified. The overview of parameters per model is easily found in the code.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide the data split in appendix C per data set. In 5.2 they state how they evaluated which metrics and take the average with 16-84th percentiles as the variation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise in false positive rate reduction and conformal prediction sets.
