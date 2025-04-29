
## Layer-Wise Adaptive Model Aggregation for Scalable Federated Learning
Sunwoo Lee, Tuo Zhang, A. Salman Avestimehr
Keywords: ML: Distributed Machine Learning & Federated Learning, ML: Scalability of ML Systems
AAAI/2023/Proceedings/26023 - Layer-Wise Adaptive Model Aggregation for Scalable Federated Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide no implementation source. They do extensively discuss their method with pseudo code, but general framework schematics or visualisations are not found. The only detail stated on the implementation is that they use tensorflow 2.4.3. It will be a huge effort to re-implement this.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors evaluate the method on three public data sets and provide citations. They also provide some details on how they create a data set out of one of them. Statistics on the data sets are not provided but could be easily extracted.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors introduce a couple new hyperparameters for their method. Their values are stated with each result in the table. No search method is defined, as the authors just provide the results of a (non-exhaustive) grid search.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The experimental procedure seems quite clear including their metrics regarding training, but what is meant with 'periodic aggregation' is not. Furthermore there is no note made about train/tests set, yet the results table talks about 'validation acc.'. This is confusing and should have been clearly stated in the paper.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a good understanding of federated learning, and is mathematically quite layered and complex.
