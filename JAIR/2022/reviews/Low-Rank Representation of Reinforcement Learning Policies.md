
## Low-Rank Representation of Reinforcement Learning Policies
Bogdan Mazoure, Thang Doan, Tianyu Li, Vladimir Makarenkov, Joelle Pineau, Doina Precup, Guillaume Rabusseau
Keywords: 
JAIR/2022/Proceedings/13854 - Low-Rank Representation of Reinforcement Learning Policies.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors state the code will be available on GitHub upon publication, but no link is provided. They also state the code is included wit hsupplemental files as a zip, but JAIR does not provide this online. We decided to make an exception in this case, and check GitHub.com for the title of the repository, but find nothing. A second attempt with Google, with search '$TITLE$ "GitHub"' also yields no results. The authors do provide detailed Python pseudo code in Appendix A.9.1. which also provides information on which packages are used. This makes re-implementation very accesible, but will still require some work.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use simulated environments and provide a citation on the lbirary from which they use these. It includes Continuous Mountain Car, bandit turntable and Pendulum. They are described in appendix A.9.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state HPs in table 2 of appendix A.9.3. per environment. The authors state on which objective they determined the configurations (empirically) but not under which budget.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the method with average wasserstein-1 metric and provide a formula in 5.1. They also use variance of the returns (environment) and number of parameters (model). Population is not always clear, variation and aggregation not specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on RL policies.
