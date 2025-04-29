
## Greedification Operators for Policy Optimization: Investigating Forward and Reverse KL Divergences
Alan Chan, Hugo Silva, Sungsu Lim, Tadashi Kozuno, A. Rupam Mahmood, Martha White
Keywords: 
JMLR/2022/Proceedings/21054 - Greedification Operators for Policy Optimization: Investigating Forward and Reverse KL Divergences.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

Implementation details are stated in 6.1.1. with a link to a package they use for their experiments as well as links to two implementations of simulated environments. Pseudo code given in algorithm 1 and 2. High level overview in figure 1. Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(6/6)

The authors link a source for their environment Misleading Maze in 6.2.2. They also use Microworld environments and describe them but do not provide code on the environment although it seems relatively simple. In 6.3 the authors use OpenAI gym environments, name and cite them and provide a direct link in the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameter grids being tested for each environment. The architecture of the model is also stated there. Selected hyperparameter per environment are not given. No structured overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure KL loss in figure 5 and present mean and standard eviation. In figure 6 and 7 they show the final value functions over 1000 iterates. Figure 8 shows the standard deviation over the temperature parameter. Figure 9 is averaged over 30 runs with standard errors with varying temperatur values and metric is absolute times of reaching the goal. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Reuries expertise on RL
