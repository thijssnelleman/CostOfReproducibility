
## Parts of Speech–Grounded Subspaces in Vision-Language Models
James Oldfield, Christos Tzelepis, Yannis Panagakis, Mihalis Nicolaou, Ioannis Patras
Keywords: 
NeurIPS/2023/Proceedings/70789 - Parts of Speech–Grounded Subspaces in Vision-Language Models.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide an implementation in the supplementary materials (https://openreview.net/attachment?id=hLoanbRrjM&name=supplementary_material). In the readme they state installation requirements and how to run the code. The code has okay comments and the structure is extremely easy. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use the WordNet database and provide a citation. High level statistics given in sec 3. No link, description or deeper statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

In equation 1 the authors introduce HP delta. Its set to 1/2 for all experiments in sec 3. but no acquisition is given only a a reference to an ablation study in the supplementary material.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The results are top-1 accuracy and the results are single run. No train/test split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requries expertise on vision language models.
