
## Leaky Hockey Stick Loss: The First Negatively Divergent Margin-based Loss Function for Classification
Oh-Ran Kwon, Hui Zou
Keywords: 
JMLR/2023/Proceedings/221104 - Leaky Hockey Stick Loss: The First Negatively Divergent Margin-based Loss Function for Classification.pdf
Project URL: http://github.com/ohrankwon/lhsc

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors state a link to their implementation on the JMLR website and in the introduction (https://github.com/ohrankwon/lhsc). In the readme they state installation instructions. Code needs more comments. Structure is okay.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(16/16)

The authors state download link for BUPA dataset in the implementation manual and also include a file on it. In 6.1. the authors present results on simulated data and state the simulation details, code available in the implementation. In 6.2 they use 15 datasets from UCL repository, provide a citation and direct link no description or statistics. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors use five fold cross-validation on the datasets with randomly sampling 2/3 of the data as training and 1/3 as validation to select optimal delta 'from 100 values' but its not clear which values and which are selected.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results as misclassification rates averaged over 100 runs with standard error in table 1 and table 2. 1/3 of each dataset is randomly sampledas the test set on which they report results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on loss functions and classification calibration.
