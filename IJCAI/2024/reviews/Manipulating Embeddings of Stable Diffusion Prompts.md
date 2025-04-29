
## Manipulating Embeddings of Stable Diffusion Prompts
Niklas Deckers, Julia Peters, Martin Potthast
Keywords: Methods and resources: Machine learning, deep learning, neural models, reinforcement learning, Application domains: Images, movies and visual arts
IJCAI/2024/Proceedings/0845 - Manipulating Embeddings of Stable Diffusion Prompts.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state their code is publicly available (https://github.com/webis-de/IJCAI-24). Here we have to follow the link to the actual repository (https://github.com/webis-de/ijcai24-manipulating-embeddings-stable-diffusion). The authors have a short note on how the code can be deployed and where the data can be found and how it should be placed into the repository. The authors directly refer to their paper to explain which file serves what purpose, how to run it and to what results in the paper they correspond. The code has some comments but could do with some more.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors share a direct link for the data, which is publicly available. They state in 2.4 they use a subset of another data set which they cite. They publish the used prompts publicly (the link). However few details on this are shared, such as what this data set looks like, statistics, how the subset was produced.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors state the seeds used in the implementation docs. However the parameters used are vague and not directly stated, which will have to be extracted from the implementation. No details are shared on how these values were extracted, but the references/citations could yield some information here.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state their experimental procedures in section 4 and state they show the results in figure 9 over 65 seeds, but not what aggregation strategy was done. The metrics used are explained/described in section 3.1. The authors also conduct a user study in 4.2, where they state how many participants, what the task was was and how many iterations each participant did. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires a good understanding of stable diffusion and prompt engineering to understand the task/analysis conducted.
