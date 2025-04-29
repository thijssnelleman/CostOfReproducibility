
## Guiding a Diffusion Model with a Bad Version of Itself
Tero Karras, Miika Aittala, Tuomas Kynkäänniemi, Jaakko Lehtinen, Timo Aila, Samuli Laine
Keywords: 
Award: Best Paper Runner-up
NeurIPS/2024/Proceedings/3390 - Guiding a Diffusion Model with a Bad Version of Itself.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/NVlabs/edm2). In the readme they state installation requirements, how to infer from rpetrained models with various arguments, how to calculate the metrics and reference to the code for explanation, how to download and prepare the datasets, how to train new models, how to visualise the toy example with plots, and some notes on the development and acknowledgements. The code has beautiful comments. The repository structure is overseeable due to good naming and not too many files being present as well as the examples. Pseudo code is given in algorithm 1/2 in the appendix. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use ImageNet (citation provided, direct download in implementation). Description and statistics missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors discuss HP search in appendix B.1. Here they state the parameters and their spaces considered. This was optimised using grid search (budget specified as 30k metric evaluations across configurations). The grid search strategy is given and the results are presented as the best of three evaluations with figure 3 visualising these results. There is some unclarity regarding the selected values but in general it is good enough specified in table 1 and algorithm 2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors present the results as best over 3 runs (see hpo opt) in table 1 and with variance in figure 2 (min/max FID). The metrics are FID and FD on which citations are provided but no description given. No training/testing split indicated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on diffusion models and guided training.
