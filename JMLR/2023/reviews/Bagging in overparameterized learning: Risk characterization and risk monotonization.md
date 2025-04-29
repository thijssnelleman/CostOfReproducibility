
## Bagging in overparameterized learning: Risk characterization and risk monotonization
Pratik Patil, Jin-Hong Du, Arun Kumar Kuchibhotla
Keywords: 
JMLR/2023/Proceedings/230887 - Bagging in overparameterized learning: Risk characterization and risk monotonization.pdf
Project URL: https://jaydu1.github.io/overparameterized-ensembling/bagging/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their project in section 1.3 where they link their implementation (https://github.com/jaydu1/overparameterized-ensembling/tree/main/paper/bagging). Code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors conduct numerical simulations. The model is defined on page 17. Code available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors detail their method in algorithm 1. They define several parameters (n_te, f, v, M, CEN, η) some of these values are stated in the caption of the figures not all are clear like η.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present the results over 100 dataset repitions and present it averaged + std dev. Metrics are Excess Risk (Caption of figure 1).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires epxertise on bagging.
