
## Cardinality-Minimal Explanations for Monotonic Neural Networks
Ouns El Harzli, Bernardo Cuenca Grau, Ian Horrocks
Keywords: Machine Learning: ML: Explainable/Interpretable machine learning, AI Ethics, Trust, Fairness: ETF: Explainability and interpretability, Machine Learning: ML: Theory of deep learning
IJCAI/2023/Proceedings/0409 - Cardinality-Minimal Explanations for Monotonic Neural Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state in section six that they conducted their experiments through Google Colab on CPU. The authors present pseudo code in algorithm 1. There are a few other statements regarding implementing certain methods however no practical details are given on their implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors state the datasets used in section 6, for which they provide a citation on the first, and numerical and tasks descriptions for both. More information would be welcome. The second data set has a direct link is provided. It is implied that the first datasets is publicly available through the citation details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Based on algorithm 1, the method seems to be parameter free. Although they use NNs for their experiments, these parameters aren't persay the HPs of their own method. They are presented in section 5.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors trained neural networks on the presented data sets (with specified hps) to apply their method on. They state the metric on which these NNs were optimised on, and then compute the cardinality-minal explanations. They use 'explanations sizes' and compute time as metrics. The experiment has a layer simply due to the complexity of the method, which may take a bit more effort to reproduce. This is not persay by the lack of documentation or trying by the authors (this is a choice), the description of the experiment is rather short.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on explainable AI, specifically abductive methods regarding features feature subset computation.
