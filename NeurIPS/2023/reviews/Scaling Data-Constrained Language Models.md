
## Scaling Data-Constrained Language Models
Niklas Muennighoff, Alexander Rush, Boaz Barak, Teven Le Scao, Nouamane Tazi, Aleksandra Piktus, Sampo Pyysalo, Thomas Wolf, Colin Raffel
Keywords: 
Award: Outstanding Paper Runner-Up
NeurIPS/2023/Proceedings/3426 - Scaling Data-Constrained Language Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/huggingface/datablations). The readme indexes the readme, provides extensive details on the data and how to run the code, where to download models, how to train, how to evaluate. Installation notes not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use the C4 dataset and provide a citation on it. Details regarding their filtering procedure given in appendix N and the code is available in the implementation. Direct link given in the readme. Details on the dataset are a bit lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors discuss hyperparameter values in appendix S. Model architecture overview given in table 15. Acquisition is that they took most values from previous work. A bit of effort is still needed to get an overview of all used parameters and defend against their sources.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use a train, validation and test set. Its not clear how tihs was split. The metrics are validation/test loss. Results are presented per model (No aggregation/variation). In figure 6 they state they repeated each experiment with different seeds (amount not clear) and the variation is std dev but aggregation is not given.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on LLMs.
