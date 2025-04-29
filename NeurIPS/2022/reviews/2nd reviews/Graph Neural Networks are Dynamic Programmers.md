
## Graph Neural Networks are Dynamic Programmers
Andrew J Dudzik, Petar Veličković
Keywords: 
NeurIPS/2022/Proceedings/53143 - Graph Neural Networks are Dynamic Programmers.pdf
Project URL:

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

Starting with 4 since ''The code and the data are proprietary'' and not provided. I did not find a specification for programming language, the framework or other details. However, the authors state that ''The data generation and base model implementation is publicly available within the CLRS benchmark. We detail the model extensions we made'' and thus, I did not add any other points.
They do not provide pseudocode or figures about the code, so +2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

The authors use the CLRS benchmark and provide a citation, but not direct link: +1. The authors have a brief description of the benchmark. I could not find statistics of the benchmark, +1. The dataset is not private.
The authors say they use ''exactly the data generation'' of the CLRS benchmark, so no extra points of synthetic data generators.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors do not summarise the hyperparameter space, but refer to the CLRS benchmark. I don't think this benchmark talks about the hyperparameter space, so +3.
Regarding the values and how they are acquired, the authors again refer to the CLRS benchmark and say that hyperparameters are stated there, so I trust them that this information is there but its not part of the documentation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

1. I think for people in the field, it could be obvious which metrics are used with the CLRS benchmark, but it is not stated explicitly, not even in table 1 and 2 with results, so +2. 
2. Train and test split should be clear from the CLRS documentation referred to.
3. The strategy used to acquire the evalations should be clear.
4. The results are clearly aggegated in table 1+2.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

The paper contains a decent amount of theory and touches upon many fields, e.g. GNNs, Dynamic programming.