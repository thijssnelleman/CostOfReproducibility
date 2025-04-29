
## Increasing Confidence in Adversarial Robustness Evaluations
Roland S. Zimmermann, Wieland Brendel, Florian Tramer, Nicholas Carlini
Keywords: 
NeurIPS/2022/Proceedings/55120 - Increasing Confidence in Adversarial Robustness Evaluations.pdf
Project URL: https://zimmerrol.github.io/active-tests/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation on their project page (https://github.com/google-research/active-adversarial-tests). In the readme they state the method. There are no installation instructions, code can use more comments. Structure is small. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors state the dataset used in the checklist and appendix B. They provide a citation on it.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Parameter values for their method are stated in appendix B. They are structured available per method in the case_studies directory. The test threshold is chosen to be 0.95. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the methods on the test set of CIFAR-10. Results are single model. Metric is the binarization test performance (defined). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on adversarial robustness.
