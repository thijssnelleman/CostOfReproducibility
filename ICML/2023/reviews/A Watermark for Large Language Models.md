
## A Watermark for Large Language Models
John Kirchenbauer, Jonas Geiping, Yuxin Wen, Jonathan Katz, Ian Miers, Tom Goldstein
Keywords: 
Award: Outstanding Paper
ICML/2023/Proceedings/541 - A Watermark for Large Language Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/jwkirchenbauer/lm-watermarking). In the readme they describe the repository, provide a demo, a lengthy description of hyperparameter, how to use their code. Installation requirements file provided. The comments are good but the structure is huge and can use a better index.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(1/1)

The authors use the C4 datase REalNewsLike and provide a citation. No other details provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

There are some notes on hyperparameter temp in appendix C. There are more hyperparameters described in the readme of the implementation. Some values can be found throughout the text, but an overview is missing and acquisition is not always clear. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate z-score and PPL (not explained) averaged over 500 sequences / 200 tokens, and also present ROC curves. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on LLMs
