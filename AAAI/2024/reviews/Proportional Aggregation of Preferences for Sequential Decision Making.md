
## Proportional Aggregation of Preferences for Sequential Decision Making
Nikhil Chandak, Shashwat Goel, Dominik Peters
Keywords: GTEP: Social Choice / Voting
Award: Outstanding paper award
AAAI/2024/Proceedings/29553 - Proportional Aggregation of Preferences for Sequential Decision Making.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide no source of their implementation. They state they evaluate their decision making method on various data sets and run experiments regarding training preference models but none of this implementation is given. However, the authors method is relatively straight forward in implementation terms. No details are given in the paper, which could have helped independendent investigators, which will have to start from scratch.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(3/3)

The authors use a synthetic data set which they cite a setup source for and explain the parameters used for it, but the actual implementation of the generator is not given. They also use a politcal data set and provide a source for where to acquire it, and they provide a short description but general metrics seem to be missing. Last is a public data set called moral machine, which is cited but no metrics/details are provided other than a description of the task.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The fitted model (Plackett Luce) could be parameter free: The authors give no details on any parameters. However, this would have to be determined by the independent investigators by following their citation to this model. If this was clearly stated in the paper, or implementation documentation was provided, this cost could easily have been 1.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors provide a lot of details on each experiment they conduct regarding the number of decision being made, thus reproducing this experimental setup should in general be quite attainable, however there are a lot of settings to this experiment and metrics to be applied/recorded/calculated as well.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method itself is generally straight forward, however understanding the context of the method may take some time.
