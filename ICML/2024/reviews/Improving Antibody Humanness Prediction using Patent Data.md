
## Improving Antibody Humanness Prediction using Patent Data
Talip Ucar, Aubin Ramon, Dino Oglic, Rebecca Croasdale-Wood, Tom Diethe, Pietro Sormanni
Keywords: 
ICML/2024/Proceedings/32845 - Improving Antibody Humanness Prediction using Patent Data.pdf
Project URL: https://github.com/AstraZeneca/SelfPAD

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/AstraZeneca/SelfPAD). In the readme they provide an introduction to the method, an index on the readme, installation regarding the code, explanation on the configuration files, explanation of entry points regarding train/tune/test, overview of the repository structure, explanation of what the output structure looks like, and some citations information. The code is rich in comments. Figure 1 gives an overview of the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors use four different datasets each with lengthy descriptions, key staistics including more indepth (table 1) and citations. The authors state they use three datasets as benchmarks, and the test set of the fourth as well. They all seem to be publicly available. There are no direct links provided to the data. The authors state details on the implementation in the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors summarise the configuration in their implementation, as well as in their paper (table 9) per section of the experiment, stating this setup is fixed. The authors state they did a hyper-parameter sweep in appendix B and what it was optimnised on ('human search'). This was conducted for both phases of the experiment. The budget is not mentioned.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they randomly split the training and testing sets using stratified sampling. 3 out of four data sets are used as test sets. The authors also state their procedure to avoid data leakage. The authors use various metrics in table 2, but they are all standard. The test sets are static, no other pluralities specified so all results are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires experience in the task (biomedical) to understand what exactly the problem is and what kind of solution the authors present. Other than that, although the method is layered, each step is quite accesible. 
