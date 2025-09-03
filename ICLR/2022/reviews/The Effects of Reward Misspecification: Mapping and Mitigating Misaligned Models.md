## The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models
Alexander Pan, Kush Bhatia, Jacob Steinhardt
Keywords: 
ICLR/2022/Proceedings/6579 - The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to base implementation and data in section 1 (https://github.com/aypan17/reward-misspecification). In the readme they state each repo has its own requirements and provide a seperate readme for each, stating underwhich conditions they have been tested, including links to other implementations they based it off. Each seperate readme has examples of how to run the code. The main code of the authors themselves is in the scripts directory which is well documented.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors main contribution are four RL environments. The environments are provided in the implementation and are detailed in 3.1. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors run baselines on their new environments to 'systematically study reward hacking' and the authors state they adopt the original works HP values when available in section 3. The values are documented in the implementation with descriptions, although a more centralised structure would be welcome to find the values.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors measure environment reward as well as AUROC and Max F-1. Results are over single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
