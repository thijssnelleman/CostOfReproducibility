
## Decorrelated Variable Importance
Isabella Verdinelli, Larry Wasserman
Keywords: 
JMLR/2024/Proceedings/220801 - Decorrelated Variable Importance.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

Implementation for the simulations is not provided, but they do state two R packages used in section 4.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(5/5)

The authors use simulated data and state the formulas used with parameters in section 4. Implementation not given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors state they use default settings for the Random Forest models in section 4 from the R package and do not tune these. There is however no overview of these parameters or what these values are and would have to be determined by inspecting the package. However as no version is stated, this could lead to difficulties.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure correlection over coverage. X-axis steps not given in figure 2. In figure 3 they present confidence intervals over 100 simulations. Table 2 presents coverage results and the standard error is stated in the caption. No data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on correlation, nonparametric estimation and variable importance.
