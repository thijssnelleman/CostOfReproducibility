
## How to Trust Your Diffusion Model: A Convex Optimization Approach to Conformal Risk Control
Jacopo Teneggi, Matthew Tivnan, Web Stayman, Jeremias Sulam
Keywords: 
ICML/2023/Proceedings/24442 - How to Trust Your Diffusion Model: A Convex Optimization Approach to Conformal Risk Control.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their implementation (https://github.com/Sulam-Group/k-rcps). In the readme they introduce the method and provide a link to zenodo for model checkpoints. There are no installation instructions. There are very few comments. The code could use an index as the structure is quite large.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(2/2)

The authors use two datasets for their experiments on which they provide citations. Direct links and descriptions with some statistics can be found in appendix D.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors describe the input to their algorithm in algorithm 1. Various model parameters are stated in experiment section. A full summary on the parameters used, space considered and acquisition is not found. This was also not found with some effort in the implementation.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure uncertainty which they explain section 4. They measure over 20 independent 'draws' the mean interval length, the variance seems to be standard deviation. Train test split not applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on diffusion models, CV, generative AI and risk.
