## Preserving Fairness in AI under Domain Shift
Serban Stan, Mohammad Rostami
Keywords: 
JAIR/2024/Proceedings/16694 - Preserving Fairness in AI under Domain Shift.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors present their implementation online https://github.com/rostami-m/FairUDA/. There are no details regarding installation requirements, how to execute, ... (just a second readme with minimal information). That is why I increase the costs by 1. More than 50 percent of the code is without meaningful comments. (+1) The structure is not difficult to navigate, but it is just a zipfile that you have to download that contains all the files. That is why I increase by 1. There is pseudo code. 


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

3 data sets and all of them are public. There are direct links to the data sets. There are descriptions with statistics for all three data sets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

They mention the hyperparameters for training in 5.1.5 Training and Model Selection and they are stated in the implementation. I do not see an overview. (+1) 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

They cite a survey as a reference for the metrics. They describe the procedure for splitting the data set and I think the seed is given in the implementation. I think they fulfilled all the criteria. 


### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

I would rate the level of expertise with 4. It is combining two-different fields. However, they introduced a lot of concepts and I think if you have basic knowledge about machine learning it is accessible.
