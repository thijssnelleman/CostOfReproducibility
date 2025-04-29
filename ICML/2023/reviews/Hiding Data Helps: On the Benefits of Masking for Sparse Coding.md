
## Hiding Data Helps: On the Benefits of Masking for Sparse Coding
Muthu Chidambaram, Chenwei Wu, Yu Cheng, Rong Ge
Keywords: 
ICML/2023/Proceedings/24288 - Hiding Data Helps: On the Benefits of Masking for Sparse Coding.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide three pieces of pseudo code. The authors provide a link to their implementation (https://github.com/2014mchidamb/masked-sparse-coding-icml). In the readme the authors specify how to run the experiments. There is an requirements list available for installation. There are config files available for various experiments. There is a good amount of comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors state they generate datasets for their experiments. The generator code is available in the implementation. The parameters are specified in section 4 and 4.1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide configuration fiels per experiment and state they did not perform extensive HP tuning and found their settings worked fine ('low budget', 'human opt'). The values are also summarised in section 4. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metric in formula 2.1 (sec 2.1). The training results are presented over epochs where each experiment is repeated five times and presented as mean + std dev.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on spare coding and the theory behind it.
