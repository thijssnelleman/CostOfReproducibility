
## Debating with More Persuasive LLMs Leads to More Truthful Answers
Akbir Khan, John Hughes, Dan Valentine, Laura Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward Grefenstette, Samuel Bowman, Tim Rocktäschel, Ethan Perez
Keywords: 
Award: Best Paper
ICML/2024/Proceedings/2269 - Debating with More Persuasive LLMs Leads to More Truthful Answers.pdf
Project URL: https://github.com/ucl-dark/llm_debate

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/ucl-dark/llm_debate). In the readme the authors provide installation instructions, execution examples / tutorials, explanation on the data and how to use it with the code and an explanation on the repository structure. The code has an acceptable amount of comments (but more would be welcome). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use one dataset for which they provide an explanation, citation, key statistics (the static train/test split) and extended filtering details in appendix D. Extensive statistics on the data are missing. The data is available in the implementation docs.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors discuss hyperparameters in table 4 and 5 which present the configuration of the experiment (tournament). Other than that, configurations do not apply to this method as the authors present an analysis on various LLMs.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use ELO ranking (explained in D.5), accuracy, win / coverage rate, and other standard statistical terms / task specific metrics. The authors state how the data is divided in training and testing data in 2.2. The authors explain the tournaments and experiment set up in great details, including a scheme on it in figure 2. The authors state how many matches are produced in the tournament. The aggregations/variations are explained under each image.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires some expertise on LLMs/NLP but is in general quite accessible. The exteremly detailed appendix means very little external resources are needed.
