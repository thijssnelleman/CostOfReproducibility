
## ViT-CX: Causal Explanation of Vision Transformers
Weiyan Xie, Xiao-Hui Li, Caleb Chen Cao, Nevin L. Zhang
Keywords: Computer Vision: CV: Interpretability and transparency, AI Ethics, Trust, Fairness: ETF: Explainability and interpretability, Machine Learning: ML: Explainable/Interpretable machine learning
IJCAI/2023/Proceedings/0174 - ViT-CX: Causal Explanation of Vision Transformers.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/vaynexie/CausalX-ViT). An overview of the method is presented in figure 3. In the readme they state they provide a requirements file for the code, details on a testing environment, a main entry point for the code and details on the hyperparameters for the method. There is an example notebook showing usage of the method. The code has quite a lot of comments. The repository structure is small and easy to oversee. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/4)

The authors state the four datasets used in 4.2, where they state they used the validation set of the cited dataset. Only one dataset is clearly stated to be public. There are no direct links or details stated otherwise on the dataset. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors discuss hyper-parameter settings in 4.2. Here they state the values of various parameters. The hyperparameters the authors consider are also stated in the implementation docs, but no acquisition strategy is specified. The authors do an ablation study in 4.4. and state there is a hyperparameter sensitivity analysis in the appendix (They state section F but it seems to be E). Here they show the impact of changing the values of various parameters on a grid over the metrics. This gives some indication of the values tried empirically by the authors.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the evaluation metrics in 4.1 and provide citations on them. They state they follow protocol of previous methods, suggesting theey are standard in this subfield. The metrics are explained afterwards with a paragraph on each. The results indicate single model results. The authors state their method is training free yet refer to the parameters as hyper-parameters which is a bit confusing. The authors state in 4.2 the experiment is done on 5000 randomly selected images from the validation set of the data.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries experience with SOTA of explainable AI in CV.
