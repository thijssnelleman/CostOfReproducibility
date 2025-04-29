
## Bayesian Multinomial Logistic Normal Models through Marginally Latent Matrix-T Processes
Justin D. Silverman, Kimberly Roche, Zachary C. Holmes, Lawrence A. David, Sayan Mukherjee
Keywords: 
JMLR/2022/Proceedings/19882 - Bayesian Multinomial Logistic Normal Models through Marginally Latent Matrix-T Processes.pdf
Project URL: https://github.com/jsilve24/fido_paper_code

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation in section 4 and on the JMLR website (https://github.com/jsilve24/fido_paper_code). There are some working notes in the readme. No installation notes. Code has okay comments. Structure could use some explanation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors conduct simulation studies in section 5 and provide equations, state the parameters and their values and code is available in the implementation ('generate_data.R'). In section 6 the authors use a dataset on Crohn's Disease and provide a description and citation but no link or statistics. In section 7 the authors simulate an artifical gut model and provide equations and state from which package they used it and a citation but more details on it would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyerp-parameters and their values in appendix H/I/J. The acquisition is not clear for each.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Results are presented with mean and 50%/95% credible regions over 4 independent models in figure 3. In figure 2 the authors show multiple levels of credible interval over various classes. Figure 1 shows various settings of the simulator and measure the percent of counts that were zero and the RMSE of regression coeffiecients and each point is a single run. Data split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on bayesian statistics and multivariate analysis.
