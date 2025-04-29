
## Semi-Supervised Deep Regression with Uncertainty Consistency and Variational Model Ensembling via Bayesian Neural Networks
Weihang Dai, Xiaomeng Li, Kwang-Ting Cheng
Keywords: ML: Semi-Supervised Learning, CV: Learning & Optimization for CV, CV: Medical and Biological Imaging, APP: Healthcare, Medicine & Wellness, ML: Bayesian Learning, ML: Classification and Regression, ML: Deep Neural Network Algorithms, RU: Bayesian Networks
AAAI/2023/Proceedings/25890 - Semi-Supervised Deep Regression with Uncertainty Consistency and Variational Model Ensembling via Bayesian Neural Networks.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/xmed-lab/UCVME). In their repository they provide an overall framework, instructions on where to get the data set from, a requirements list regarding other libraries, how to run training/testing commands, where to get pretrained models and some contact details. The code has some comments but seems a bit difficult to follow. The authors also provide us with a supplementary details in the repository which definitely helps re-implimentation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use two data sets. Both are a public data set which they cite, provide a description on an, give key statistics and an example on. In the supplementary there are loads more details and statistics provided. They also provide us with a direct download link for the data. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors provide for each data set the hyperparameter values for their method under the settings section. They state the values were selected empirically, but not how many evaluations they invested to determine them.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state each experiment is run five times with mean + std dev. The metrics are only briefly noted. The data set split is clearly explained and not randomised.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries an understanding of bayesian neural networks.
