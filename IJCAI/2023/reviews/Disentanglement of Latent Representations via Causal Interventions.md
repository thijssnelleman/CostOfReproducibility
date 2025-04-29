
## Disentanglement of Latent Representations via Causal Interventions
Gaël Gendron, Michael Witbrock, Gillian Dobbie
Keywords: Knowledge Representation and Reasoning: KRR: Causality, Computer Vision: CV: Representation learning, Machine Learning: ML: Autoencoders
IJCAI/2023/Proceedings/0361 - Disentanglement of Latent Representations via Causal Interventions.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors share a link to their implementation (https://github.com/Strong-AI-Lab/ct-vae). In the readme they introduce the method, discuss the datasets with direct links, and an explanation for one. There are data construction instructions, installation instructions, how to run experiments, what the structure of the config files is, how to access the logs and how to tune the hyperparameters.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The data is present in the implementation, directly linked or explained how to extract otherwise. In the paper they state each data set with a descriptions and a citation. They also show key details on the data distribution in figure 4. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors share their hyperparameter search script in the implementation. Here the search space definitions can be found, as well as in the configs_hyp directory. The actual values can be found in the configs directory, although it will take a good eye to determine which belongs to which experiment due to the sheer quantitiy of them. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The experiments are quite complex to grasp and require domain knowledge to understand. This could be eleviated in part with lengthier explanations, but is not required: It is simply a choice for the authors and in this case in part unavoidable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method presented and experiments conducted require a good understanding to fully grasp the information presented. However the complete documentation of the implementation and experiments alleviates this cost. 
