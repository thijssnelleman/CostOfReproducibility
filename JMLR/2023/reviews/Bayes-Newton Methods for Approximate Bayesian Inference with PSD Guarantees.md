
## Bayes-Newton Methods for Approximate Bayesian Inference with PSD Guarantees
William J. Wilkinson, Simo Särkkä, Arno Solin
Keywords: 
JMLR/2023/Proceedings/211298 - Bayes-Newton Methods for Approximate Bayesian Inference with PSD Guarantees.pdf
Project URL: https://github.com/AaltoML/BayesNewton

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website (https://github.com/AaltoML/BayesNewton). In the readme they state a description, installation instructions, getting started with examples, and a list of available models. Code has fine comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors conduct three case studies in 8.4. which are on simulations/models. They are described with formulae and parameters and visualised in figure 2. Code available in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The pseudo code of the algorithms is given in appendix H. The authors detail the hyperparmaeter values informalyl in the text of each experiment. Acquisition not completely clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors perform 4-fold cross validation and present the mean in fig 3, 5. In figure 7 they show the mean across 4 synthetic datasets. They plot training loss, Test NLPD (defined in 8.4) and ground Truth RMSE. Its not completely clear where the test set comes from in the last experiment.  

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requries expertise on gaussian processes
