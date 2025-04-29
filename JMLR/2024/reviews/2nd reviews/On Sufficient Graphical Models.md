## On Sufficient Graphical Models
Bing Li, Kyongwon Kim
Keywords: 
JMLR/2024/Proceedings/230893 - On Sufficient Graphical Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The paper includes link to a GH Repository. This repository includes a single R file. There is no information on how to run this file, how to set up the environment, how the results are obtained, etc. The single file has only a few comments that structure the different parts of the code. 


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

For their simulation experiments, they state which models they used and how they are were parameterised. However, they do not provide code. I believe that for experts of the field, the information they give is sufficient. 
In addition, they evaluate on the DREAM 4 dataset. There is no direct link, but a citation as well as a brief description. There are no statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

Their method requires the choice of a kernel as well as the tuning of three constants of the method. The constants are chosen according to a cross validation for thresholding or a grid search for the \eps parameter. They provide the search space for their HPO informally in the text. There is no table of hyperparameter choices and the final values are not stated. However, the parameter choices seem to happen automatically or on the fly. The budget for which the acquisition is done is not known.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Authors evaluate regarding the ROC score, which they introduce in sufficient detail. They do not conduct any dataset splits since their method does not require training. For aggregation, they take the mean over a given number of iterations. No information on the statistical distribution of results is given. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

The paper is mostly written towards specialised readers from the field. The problem is not really explained well and the paper is overall very theoretical. Further, they only provide a very rough implementation of evaluated models in R. To setup experiments, acquire datasets and run the evaluation, major knowledge in the field is required.
