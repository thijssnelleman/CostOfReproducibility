
## Redefining Contributions: Shapley-Driven Federated Learning
Nurbek Tastan, Samar Fares, Toluwani Aremu, Samuel Horváth, Karthik Nandakumar
Keywords: Machine Learning: ML: Federated learning, Computer Vision: CV: Bias, fairness and privacy, Machine Learning: ML: Trustworthy machine learning, AI Ethics, Trust, Fairness: ETF: Trustworthy AI
IJCAI/2024/Proceedings/0554 - Redefining Contributions: Shapley-Driven Federated Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/tnurbek/shapfed). Here they provide in the readme an overview of the method, installation instructions, and brief explanation on how to run the code. The code has some comments, and the file/directory structure is relatively simple and easy to oversee. The code automatically downloads/generates the data. Pseudo code is given in the paper, as well as an overview on the algorithm in figure 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The implementation documentation downloads/generates for cifar10. The author state they use three data sets, with descriptions, citations and statistics. The downloading insturctions are only given for cifar10, for the others this needs to be figured out with a bit of effort.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide the hyperparameter values per data set. It is not stated how these values are acquired. Parts of the hyperparameters can be found (hardcoded) in the implementation documentation. It is not specified how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use accuracy and balanced accuracy as metrics. The authors state how the data is used/distributed in their training strategies, and the training/testing split is specified per data set (static). The results seem to indicate single runs/models but this requires some effort to verify (using the implementation docs for example). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method requires a good understanding of federated learning and data/statisical biases to grasp the task. The documentation is quite complete which lowers the expertise required as authors can rely more on the presented work.
