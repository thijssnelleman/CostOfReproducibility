
## Dynamic Evaluation of Large Language Models by Meta Probing Agents
Kaijie Zhu, Jindong Wang, Qinlin Zhao, Ruochen Xu, Xing Xie
Keywords: 
ICML/2024/Proceedings/34607 - Dynamic Evaluation of Large Language Models by Meta Probing Agents.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/microsoft/promptbench). In the readme the authors state news, introduce the method, what they provide with citations, how to install as a library/package or from the repository, how to use the code, where to find tutorials for evaluation testing etc., a list of components/models/attacks/etc, a link to their benchmark results, acknowledgements, references and details on how you can contribute. The code is perfectly documented. The authors show the design of their method in figure 2. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(4/4)

The authors use four datasets for evaluation, provide citations on them and describe them with statistics in appendix A. All datasets are available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors introduce a new evaluation method. This evaluation method has probing agent and they call it a dynamic configuration. For this they set the 'temperature' as probing and judging agents as 0.7 and 0 respectively but these parameters seem to be related to the model and not their method. It seems their own method only has the number of agents as parameter, and this seems to be not fully clarified in the experiments.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors benchmark various LLMs on the datasets using their evaluation metric. No training/testing split applies. The evaluation metric is accuracy. The results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise with MAS, LLMs. 
