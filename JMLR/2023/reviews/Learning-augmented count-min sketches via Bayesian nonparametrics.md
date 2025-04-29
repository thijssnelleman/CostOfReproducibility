
## Learning-augmented count-min sketches via Bayesian nonparametrics
Emanuele Dolera, Stefano Favaro, Stefano Peluchetti
Keywords: 
JMLR/2023/Proceedings/210096 - Learning-augmented count-min sketches via Bayesian nonparametrics.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors link a library in section 4.1 regarding the optimization procedure. Pseudo code in algorithm 1. No other details.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors conduct a study on 10 generated synthetic datasets and specify the parameters. Implementation not given. In 4.2 they use synthetic and real data, each of which is named with a direct link and statistics are provided but description are not.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors conduct optimization via AX library and evaluate the objective function 50 times per dataset (budget). Its unclear how and which parameters are optimised and what the resulting values are.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use MAE as metric and present singular results. Evaluation seems to be on entire dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

Requries expertise on bayesian non parametrics.
