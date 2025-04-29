
## Probabilistic Inference in Language Models via Twisted Sequential Monte Carlo
Stephen Zhao, Rob Brekelmans, Alireza Makhzani, Roger Grosse
Keywords:
Award: Best Paper
ICML/2024/Proceedings/1903 - Probabilistic Inference in Language Models via Twisted Sequential Monte Carlo.pdf
Project URL: https://github.com/Silent-Zebra/twisted-smc-lm

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors present a link to their implementation (https://github.com/Silent-Zebra/twisted-smc-lm). In the readme they state installation instructions, general information/notes on the implementation and very extensive examples on how to run the commands for the experiments. The code has a decent amount of comments. There are a lot of code files on some seem 'archived', it would be good to have an index on these to oversee the structure of the implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors generate data from a pretrained model using a specified prompt. The models used for generation are public, and all code regarding this generation is available in the implementation. This makes it very similar to a simulated environment, and will treat it as such. The details regarding the generation are clear, the code is available (with examples). 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state experiment details in appendix G.4. They state the parameters there and that they 'did not tune hyperparameters because we found this setting to work well, and we are not comparing across different learning methods' (Human opt, budget = 1 implied). Many values are specified in the appendix, but a full summary over the considered space is not found. However in the implementation all possible arguments are summarised, giving this overview nonetheless.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state in appendix G they repeated each experiment 20 times over random seeds and report the average + 95% confidence over these repitions for the first experiment. For the second experiment, 5 repitions are done with KL divergence and 95% confidence interval. The used metrics are quite complex (KL divergence) but discussed at length in section 4 and the appendix. Train/test set split does not apply (training values discussed). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires extensive experience with LLMs/NLP, training procedures and statistical distributions. 
