
## Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution
Aaron Lou, Chenlin Meng, Stefano Ermon
Keywords:
Award: Best Paper
ICML/2024/Proceedings/947 - Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution.pdf
Project URL: https://github.com/louaaron/Score-Entropy-Discrete-Diffusion

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/louaaron/Score-Entropy-Discrete-Diffusion). In the readme the authors index and explain a few code files, detail how to install, where and how to download pre-trained models, how to run the code with parameter explanations, how to train models, explanation on the output structure and direct links to repositories their work builds on. The code could do with a some more comments. The authors give an explanation on the implementation in 5.1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use five datasets in their paper. They seem to automatically download in their code (direct link). No citations or statistics are given, only single sentence descriptions.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors present a new loss function in their paper. The authors do not discuss parameters for this loss function and refer for the used baselines (on which they apply their method) for the HPs presented there.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state they report BPC as a metric, but do not explain what this entails / how this is calculated. The authors state they report on the test sets in the appendix, except for wikitext2 where they report training set. The results seem to be single runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise with NLP/LLMs.
