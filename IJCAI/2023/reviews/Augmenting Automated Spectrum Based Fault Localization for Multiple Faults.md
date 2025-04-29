
## Augmenting Automated Spectrum Based Fault Localization for Multiple Faults
Prantik Chatterjee, Jose Campos, Rui Abreu, Subhajit Roy
Keywords: Knowledge Representation and Reasoning: KRR: Diagnosis and abductive reasoning, Multidisciplinary Topics and Applications: MDA: Software engineering
IJCAI/2023/Proceedings/0350 - Augmenting Automated Spectrum Based Fault Localization for Multiple Faults.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors share a link to their implementation (https://github.com/prantikchatterjee/ArtemisIJCAI23). In the source code readme they state the installation requirements, on what system they ran their code, the repositories they used for spectrum generation, details on the preprocessing, and a description of each code file in the directory. The code has very few comments. Although the repository is quite small, it will take some effort to understand the flow because of how the code is documented inside the files. The authors provide three pieces pseudo code and an overview in figure 2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(9/9)

The authors state the repositories used for spectrum generation in their implementation. They state in section 5 they use six repositories from an open benchmark suite with citation. They state several statistics and details and describe the data. From this data they collect spectrums (which they provide a citation on), and they state in table 2 details/statistics on the sepctrums used. This is the processed data used as actual input. All in all this process is well documented, however more details on the raw data would be welcome in regards to comparability. There is no direct link for the raw dataset.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors present hyperparameter choices as one of the research questions in section 5. They evaluate this in 5.2 for five hyperparameters and state they do a grid search, for each the grids are stated. They optimise the EXAM score on average on the training data. They use the incumbent (stated) for the rest of the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

In section 5.1 the authors state the evaluation metrics with explanations and citations. The authors state they use k-fold cross validation with six folds in section 5.2. In section 5.3 they state the tests to use to compare against other methods, the presented values (mean + std dev). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires some expertise on the task, but the method is very well documented so although the complexity is quite high this substantially lowers the requirements of other documents/expertise.
