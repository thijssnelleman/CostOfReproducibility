
## Randomized Confidence Bounds for Stochastic Partial Monitoring
Maxime Heuillet, Ola Ahmad, Audrey Durand
Keywords: 
ICML/2024/Proceedings/32731 - Randomized Confidence Bounds for Stochastic Partial Monitoring.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors present their implementation online (https://github.com/MaxHeuillet/partial-monitoring-algos). The authors provide a requirements.txt file and installation experiments. They also specify the paths to the files to run the experiments. No datasets were used. The repository has many files and is hard to navigate. Files have no comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

The authors did not use downloadable datasets but synthetic ones. They provided code and described the generation mechanism, however exact details are missing.

### Configuration
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors provide information on the hyperparameters used but not on the tuning process.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors explain the performance metric and perform statistical test. The method requires no training and therefore a split is not required. The authors did 96  repetitions and aggregate over wincount.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The paper is in a specialised field. While the authors claim to provide code to reproduce the results, these jupyter notebook seem to result in very different figures. I therefore expect large effort to fully reproduce.