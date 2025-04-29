
## Community detection in sparse latent space models
Fengnan Gao, Zongming Ma, Hongsong Yuan
Keywords: 
JMLR/2022/Proceedings/201036 - Community detection in sparse latent space models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The paper misses any reference to implementations of their method. Further, they do not state how they implemented their method to run the presented experiments. 
However, the algorithm is stated in reasonably well-understandable pseudo-code, from which, i assume, an expert could reimplement their method given enough time and effort. 


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

For their simulation experiments, they state reasonably well how the data was attained. This should be doable for an expert. However, they did not link or cite any implementations for the creation of the data. Parameter choices are present.
The real-world datasets are referenced through citations, but not through links. Those datasets seem to be public. For some of the datasets (the seemingly more commonly used ones), they do not state statistics and only give very brief descriptions. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The only hyperparameter of their method seems to be the number of refinement generations. Those are stated. It is not stated how those numbers were chosen and under which budget. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metrics are defined, but some could be better explained (e.g. Bayes risk). Since there is no training phase, we do not penalise for missing dataset splits. Aggregation is well defined (the name number of repetitions over which the mean is taken).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

The paper is mostly written towards specialised readers from the field. The problem is not really explained well and the paper is overall very theoretical. Also, the implementation of the method can only be done by scholars that are very familiar with the field (e.g. in terms of datasets, experiment setup, no code present, ...).
