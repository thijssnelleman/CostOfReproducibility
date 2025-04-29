
## Effectiveness of Vision Transformer for Fast and Accurate Single-Stage Pedestrian Detection
Jing Yuan, Panagiotis Barmpoutis, Tania Stathaki
Keywords: 
NeurIPS/2022/Proceedings/53392 - Effectiveness of Vision Transformer for Fast and Accurate Single-Stage Pedestrian Detection.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not publish their code and do not motivate it in the checklist. Overview given in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use the Caltech and Citypersons public datasets, cite them, provide descriptions on them with high level statistics. No direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors summarise the HPs in 4.1 informally. No overview or acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use thet static data splits given by the dataset for Citypersons, and Caltech is augmented with '10 folds' to a specified amount of instances in the tvt. Metrics are given in 4.1. Datasets used per result is specified in the caption. Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on vision transformers.
