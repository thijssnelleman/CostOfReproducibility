
## Discrete Key-Value Bottleneck
Frederik Träuble, Anirudh Goyal, Nasim Rahaman, Michael Mozer, Kenji Kawaguchi, Yoshua Bengio, Bernhard Schölkopf
Keywords: 
ICML/2023/Proceedings/24621 - Discrete Key-Value Bottleneck.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide an overview on their method in figure 1 and 2. They provide a link to their implementation in appendix C (https://github.com/ftraeuble/experiments_discrete_key_value_bottleneck). The readme contains installation instructions, steps to reproduce the experiments with seperate notebooks, and how to run a single experiment. The code has very few comments. The structure is easy to oversee.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors use CIFAR10 and imagenet on which no citations are provided nor descriptions/statistics/direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors have large configuration files on their experiments in the implementation. This could be used as a starting point. There are some notes on parameter values in the additional experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate model accuracy over epochs in figure 3, loss on train set in fig 4, accuracy in fig 5. The experiments are repeated with five random seeds. The aggregation/variance is not explained.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on learning under distribution shifts.
