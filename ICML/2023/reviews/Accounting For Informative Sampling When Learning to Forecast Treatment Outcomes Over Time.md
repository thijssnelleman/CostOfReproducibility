
## Accounting For Informative Sampling When Learning to Forecast Treatment Outcomes Over Time
Toon Vanderschueren, Alicia Curth, Wouter Verbeke, Mihaela van der Schaar
Keywords: 
ICML/2023/Proceedings/24146 - Accounting For Informative Sampling When Learning to Forecast Treatment Outcomes Over Time.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors publish their implementation (https://github.com/toonvds/TESAR-CDE). In the readme they index the structure of the code and directories, explain how to install, how to run the main entry point and explain the parameters + example and acknowledge other repositories they build upon. The code is rich in comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors present a new simulator which they introduce with great detail in 5.1, provide code on in their implementation. The authors present various experiments under varying parameter values.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state their hyperparameter optimisation in appendix D.2. The authors state they did bayesian optimsation over the grid of possible values in table 3. They mark the values on each grid which are optimal. Some HP values werent optimised and are only named. Some hyperparameters are hardcoded into the implementation thus making the code not completing on the entire overview of the HP set.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure the RMSE +/- standard error over various parameter values of their simulator over 10 runs. train/test split does not apply.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on forecasting and time series data + simulator construction / cancer cell simulation.
