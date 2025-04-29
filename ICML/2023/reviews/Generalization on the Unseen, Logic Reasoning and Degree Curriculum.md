
## Generalization on the Unseen, Logic Reasoning and Degree Curriculum
Emmanuel Abbe, Samy Bengio, Aryo Lotfi, Kevin Rizk
Keywords: 
Award: Outstanding Paper
ICML/2023/Proceedings/469 - Generalization on the Unseen, Logic Reasoning and Degree Curriculum.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation in footnote 2 (https://github.com/aryol/GOTU). In the readme they state and overview of codefiles. No installation instructions. Structure is simple. Comments are okay. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors eavaluate the methods over simulated data (functions) and state them in sec 4. Code available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the architectures in section 4 and can be found in the code as well (hardcoded). More details can be found in appendix B. The authors analyse the learning rate in the appendix over a grid. Their values can be found for each experiment summarised in script.sh. Not each value acquisition is explained.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors repeat each experiment 10 times and present averages. Metric is coefficient of the monomial (requires some understanding of the task). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on curriculum learning 
