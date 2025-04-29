
## MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation
Qian Huang, Jian Vora, Percy Liang, Jure Leskovec
Keywords: 
ICML/2024/Proceedings/35159 - MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation.pdf
Project URL: https://github.com/snap-stanford/MLAgentBench/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/snap-stanford/MLAgentBench/). The readme contains an overview of the method, how to install, how to run the code an an overview of the output, how to evaluate, and some file descriptions. The code has a decent amount of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(13/13)

There are some auto downloaders for the datasets present in the implementation. Each dataset has a task descriptor. The authors use various pretrained LLMs on their benchmark datasets. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method of the authors seems to be parameter free (benchmark framework).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate how well LLMs can improve ML models on benchmark data sets based on the test accuracy. In table 3 they show success rate as a metric, and how the success rate is defined. Results are single model

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience with LLMs and classic ML techniques.
