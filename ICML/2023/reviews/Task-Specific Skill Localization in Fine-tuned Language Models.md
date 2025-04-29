
## Task-Specific Skill Localization in Fine-tuned Language Models
Abhishek Panigrahi, Nikunj Saunshi, Haoyu Zhao, Sanjeev Arora
Keywords: 
ICML/2023/Proceedings/23540 - Task-Specific Skill Localization in Fine-tuned Language Models.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/abhishekpanigrahi1996/Skill-Localization-by-grafting). In the readme they provide an index of the readme, introduction to the method, installation instructions, a link to where to download the data, instructions to do before running code and an explanation on the parameters and how to run the code. The code has plenty of comments. There is no overview on the repository structure, but it is relatively simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors draw 13 tasks from GLUe, provide a citation on it and a direct download link. The authors state no statistics and a very brief description. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the hyperparmater settings in appendix A.2. The authors specify grids for two parameters. Its a bit unclear what the parameters are that are considered and how the values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate F1 and calibration error. The latter is explained in appendix A3 with a citation. The authors do not specify how the test set were acquired only that they report on them. The results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with LLMs and fine tuning.
