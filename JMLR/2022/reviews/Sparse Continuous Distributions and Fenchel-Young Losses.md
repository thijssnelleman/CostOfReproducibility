
## Sparse Continuous Distributions and Fenchel-Young Losses
André F. T. Martins, Marcos Treviso, António Farinhas, Pedro M. Q. Aguiar, Mário A. T. Figueiredo, Mathieu Blondel, Vlad Niculae
Keywords: 
JMLR/2022/Proceedings/210879 - Sparse Continuous Distributions and Fenchel-Young Losses.pdf
Project URL: https://github.com/deep-spin/sparse_continuous_distributions/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website and in the introduction (https://github.com/deep-spin/sparse_continuous_distributions/). In the readme they state installation requirements, link applications and provide a visual overview. Code has very good comments. Structure is qutie simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use the UrbanSound8k dataset (direct link, description but limited statistics), VQA-v2 (citation, link in implementation and description but limited statistics) and the breast cancer dataset (citation provided and where it was downloaded, described but limited statstics).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameter values are stated in table 6 and 7 but no acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use the official split for urbansound and vqa. The metrics are accuracy and in table 3 provide the mean and standard dev across folds, table 4 accarucy of single runs on the standard splits.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise with sparse continous distributions.
