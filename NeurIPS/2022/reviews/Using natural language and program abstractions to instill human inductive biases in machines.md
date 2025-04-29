
## Using natural language and program abstractions to instill human inductive biases in machines
Sreejan Kumar, Carlos G. Correa, Ishita Dasgupta, Raja Marjieh, Michael Y Hu, Robert Hawkins, Jonathan D Cohen, nathaniel daw, Karthik Narasimhan, Tom Griffiths
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/1294 - Using natural language and program abstractions to instill human inductive biases in machines.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

Implementation is given in the supplementary material (https://openreview.net/attachment?id=buXZ7nIqiwE&name=supplementary_material). In the readme they state the meaning of each data file and code file, where they sourced a directory of code from, and acknowledgements of other works they use. No installation instructions. The code can use better comments. The structure is very large, but with the indexing in the readme this will give some guidance.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors state they collected a dataset (GSP Boards) in 2.1. with acquisition explanation. More details on this acquisition would be welcome. Statistics are minor. It is published in the supplementary material.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide hyperparameter files in their implementation. Upon closer inspection these are python dictionaries with HP name + value structure. One is provided for each experiment type. Acquisition not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the evaluation metric in section 2.3. Variation is 95% CI over 15 trained agents or 50 humans. Aggregation not specified. The authors discuss a test set in 3.4 and this seems to be present in the supplementary materials. However more clarity would be welcome. Aggregation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on natural languages and bias.
