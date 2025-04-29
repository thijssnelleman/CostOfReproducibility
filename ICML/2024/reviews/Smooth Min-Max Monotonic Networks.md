
## Smooth Min-Max Monotonic Networks
Christian Igel
Keywords: 
ICML/2024/Proceedings/33186 - Smooth Min-Max Monotonic Networks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/christian-igel/SMM). In the Readme they introduce the method, an overview on the code structure and a toy example on how to use. The code has a decent amount of comments. The repository structure is quite large but does have an explanation on it in the readme.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use benchmark functions as data. They fix certain parameters of these functions in section 4. Furthermore, the authors evaluate the method on benchmark repository which they cite and directly link to. The authors provide extensive details on how this data was used, including in appendix B. Datasets are available in the implementation repository. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide a few HP settings in appendix B, and the authors state in the conclusion they did their experiments 'without architecture and hyperparameter tuning', and that all experiments were done with a single architecture setting. It is not clearly summarised what the parameter space is.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use 21 trials per experiment setting, and use MSE as a metric. For the dataset, the authors state they also performed 5-fold cross validation, with a 60/20/20 tvt split. The metrics are MSE aggregated by presenting the median/averaging.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on monotonic networks.
