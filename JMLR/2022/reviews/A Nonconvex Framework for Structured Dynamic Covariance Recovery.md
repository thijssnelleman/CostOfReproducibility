
## A Nonconvex Framework for Structured Dynamic Covariance Recovery
Katherine Tsai, Mladen Kolar, Oluwasanmi Koyejo
Keywords: 
JMLR/2022/Proceedings/210795 - A Nonconvex Framework for Structured Dynamic Covariance Recovery.pdf
Project URL: https://github.com/koyejo-lab/dynamicCov.git

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the introduction and on the JMLR website (https://github.com/koyejo-lab/dynamicCov.git). In the readme they state a table of contents, general info, installation instructions, how to run three examples, and references. Comments are good, structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

In section 5 the authors use simulations, in sec 6 they experiment with the motor task data set and provide a citation and a description and statistics. The simulation procedure is stated very briefly in section 5 but code is available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors describe their method in algorithm 1 and 2 of section 3. They state the tuning parameters in 3.2 but do not given an overview. The values are stated in each experiment. The authors state they conduct a grid search using 5-fold cross-validation but some details are lacking. Structured overview missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure log-euclidean metric (formula and citation given in sec 5.1.) and average it over 20 runs in table 2, table 3 does the same but with average running time, fig 2 and table 3 measures the dist^2 (e.q. 2). Variation is not stated (although there are some notes on statistical error in sec 4, this is never stated to be the resulting value). In section 6 they measure the same in section 5. Results are over a 20 sample subset of the dataset.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on dynamic covariance and time series data.
