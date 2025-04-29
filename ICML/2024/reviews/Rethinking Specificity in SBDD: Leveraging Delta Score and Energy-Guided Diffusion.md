
## Rethinking Specificity in SBDD: Leveraging Delta Score and Energy-Guided Diffusion
Bowen Gao, Minsi Ren, Yuyan Ni, Yanwen Huang, Bo Qiang, Zhiming Ma, Wei-Ying Ma, Yanyan Lan
Keywords: 
ICML/2024/Proceedings/34845 - Rethinking Specificity in SBDD: Leveraging Delta Score and Energy-Guided Diffusion.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. In figure 3 they illustrate the framework of their method. In algorithm 1 they provide pseudo code on the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors state the data set used in 5.1. which they cite in section 3. There is no real description except implicitly when they explain how they converted the data into a presentation fitting their experiment. No statistics given. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors details various parameters in algorithm 1 and state that the model phi in appendix B is a GNN. However the details regarding these parameters are not given per experiment. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors refer to the data split of another work by citation. The metrics delta is explained in formula 6, the other two (absolute and ratio) are not detailed in the paper (the concept of docking score metric is not really explained). The authors aggregate by mean and median values. Results are single run. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise in biomedical tasks (drug design) and geometric deeplearning. 
