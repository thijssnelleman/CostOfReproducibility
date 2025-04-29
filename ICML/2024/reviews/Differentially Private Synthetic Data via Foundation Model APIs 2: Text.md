
## Differentially Private Synthetic Data via Foundation Model APIs 2: Text
Chulin Xie, Zinan Lin, Arturs Backurs, Sivakanth Gopi, Da Yu, Huseyin Inan, Harsha Nori, Haotian Jiang, Huishuai Zhang, Yin Tat Lee, Bo Li, Sergey Yekhanin
Keywords: 
ICML/2024/Proceedings/34291 - Differentially Private Synthetic Data via Foundation Model APIs 2: Text.pdf
Project URL: https://alphapav.github.io/augpe-dpapitext/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/AI-secure/aug-pe). In the readme the authors introduce the method, state news updates, provide installation instructions, data download scripts and how to preprocess (also some details on the data), and how to run the code. They also list some acknowledgement repositories they used. Some of the code that isn't lend could use more comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors provide the datasets with download scripts in the implementation including citations descriptions and statistics. More details can be found in section 4. Dataset details are in appendix B.1. as well. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors place hyperparameter details in appendix B.2. They are summarised in table 13 and 14 per dataset (experiment) and in the text of b.2. No acquisition method specified. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate accuracy on the test set which is static per dataset. Results are single model/run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on NLP/LLMs and privatising data.
