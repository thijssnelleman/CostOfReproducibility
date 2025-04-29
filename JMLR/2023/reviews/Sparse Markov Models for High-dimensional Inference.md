
## Sparse Markov Models for High-dimensional Inference
Guilherme Ost, Daniel Y. Takahashi
Keywords: 
JMLR/2023/Proceedings/220266 - Sparse Markov Models for High-dimensional Inference.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors use an implementation from other authors but they do link it directly (https://github.com/david-dunson/bnphomc/blob/master/Prior_on_K_js.m). The code there is quite cryptic and its not clear what is used for what, no installation notes.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

In experiment 1 they use simulated data and provide detailed descriptions and values for it. They provide a GitHub link for the simulator. The authors use a Kaggle dataset in 4.3 and provide a direct link and a brief description but more information would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The uahotrs define various parameter values for each experiment but its not clear what is considered a parameter for their method as an overview is missing (various variables defined in algorithm 1, but no input parameters). Thus its ambigous. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present standard deviation and estimated probability. Data split not applicable. Metrics are calculated over various sample sizes n. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on markov chains.
