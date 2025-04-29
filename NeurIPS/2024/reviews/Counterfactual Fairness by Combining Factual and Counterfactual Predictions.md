
## Counterfactual Fairness by Combining Factual and Counterfactual Predictions
Zeyu Zhou, Tianci Liu, Ruqi Bai, Jing Gao, Murat Kocaoglu, David Inouye
Keywords: 
NeurIPS/2024/Proceedings/95743 - Counterfactual Fairness by Combining Factual and Counterfactual Predictions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 2 (https://github.com/inouye-lab/pcf). In the readme they state installation notes, which figure can be reproduced with what note book, how to prepare the semi-synthetic data set. Code could use some more comments/documentation. Structure is overseeable.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use a synthetic dataset in 5.1. with the formulae stated. In 5.2. they consider semi-synthetic data set with a citation and explain the dataset briefly. More details are given in appendix C. Semi synthetic data set is given raw and processed with scripts to process in the implementation. Synthetic generator is given in the notebooks. Parameters and values of the generation for each plot are there too.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The method of the authors (algorithm 1) is HP free. The pretrained predictors are discussed in appendix C.3. For the synthetic experiment this is straightforward. For the semi-synthetic only the architecture is given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use two metrics and define them over the task/experiments in section 5. The results for synthetic and semi synethetic are averaged over 5 runs. Data splits are presented in the implementation for the semi synth dataset. But its not specified and not straight away clear from the notebooks which dataset the results are produce on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on counterfactual methods.
