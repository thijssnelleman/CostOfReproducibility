
## Stealing part of a production language model
Nicholas Carlini, Daniel Paleka, Krishnamurthy Dvijotham, Thomas Steinke, Jonathan Hayase, A. Feder Cooper, Katherine Lee, Matthew Jagielski, Milad Nasr, Arthur Conmy, Eric Wallace, David Rolnick, Florian Tramer
Keywords:
Award: Best Paper
ICML/2024/Proceedings/2419 - Stealing part of a production language model.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide pseudo code on their method in algorithm 1. They provide a link to their implementation in the appendix (https://github.com/dpaleka/stealing-part-lm-supplementary). In the readme they state a short index with explanation on the code. The code has a decent amount of comments. The authors provide the data as well. Although the repository structure isnt small, it is relatively straightforward. There is an installation requirements file available. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide the data used for the experiments in their implementation including some models and some models are available online. The prompts used to attack these models are present in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The specified method (algorithm 1 and 2) is parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use root mean square as the metric between the actual model and the extracted model as metric and the model size/depth. No repeating applicable. The models each attack is conducted on is specified ('data'). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on LLMs and parameter extraction from hidden models.
