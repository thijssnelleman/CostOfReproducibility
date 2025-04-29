
## SHAP-IQ: Unified Approximation of any-order Shapley Interactions
Fabian Fumagalli, Maximilian Muschalik, Patrick Kolpaczki, Eyke Hüllermeier, Barbara Hammer
Keywords: 
NeurIPS/2023/Proceedings/72134 - SHAP-IQ: Unified Approximation of any-order Shapley Interactions.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 4 (https://github.com/FFmgll/shapiq). In the readme they state installation instructions, how to use the code, how to validate experiments. Code has okay comments. Structure is huge and needs a cleanup or an index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use the IMDB dataset (citations provided). No links, description or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Based on the code the method seems to have 4 parameters (three semantantic, one number of iterations). They are all defined for each experiment in the captions or legends.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate using MSE, MSE@K, Prec@K as metrics (standard). They evaluate on 50 random instances. Variation not explained. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on shapley interactions.
