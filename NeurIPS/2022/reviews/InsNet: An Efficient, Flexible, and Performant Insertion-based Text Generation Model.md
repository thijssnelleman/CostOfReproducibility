
## InsNet: An Efficient, Flexible, and Performant Insertion-based Text Generation Model
Sidi Lu, Tao Meng, Nanyun Peng
Keywords: 
NeurIPS/2022/Proceedings/54540 - InsNet: An Efficient, Flexible, and Performant Insertion-based Text Generation Model.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors link two repositories in the footnotes 1 and 2 of their paper that they used for the experiments. In the checklist they state the code will be released upon camera ready. This cannot be found in the paper or supplementary material. Overview given with great detail in figure 2 and more in figure 5.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use Yelp Review and News as datasets. High level statistics are given in 4.1. No citations, links, descriptions or other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Hyperparameter range of τ discussed in 4.1. The authors refer for more details on the setup to appendix ?? and more values can be found in A.1. Some grids are specified for some parameters, but the selected values from the grid are not clear. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use the BLUE/NIST metric and sequential ratio (formula given) for their results. The authors use the static data splits for tvt as defined in 4.1. Results are single model. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on NLP.
