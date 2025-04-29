
## On the Hardness of Probabilistic Neurosymbolic Learning
Jaron Maene, Vincent Derkinderen, Luc De Raedt
Keywords: 
ICML/2024/Proceedings/32766 - On the Hardness of Probabilistic Neurosymbolic Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/jjcmoon/hardness-nesy). In the readme they state installation instructions, links to the data and how to run the code. The code has few comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors provide direct download links in the implementation. The authors describe the datasets in section 7 and what subseet is used, and explain the data set directly available in the implementation. Citations are present but statitstics are missing. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method of the authors is, based on the paper and the code file 'cms_gen.py', parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the number of instances solved in the benchmark datasets over runtime. No data splits applicable. In table 2 they present the cosine similarity between gradients including standard deviation. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise with SAT solving and gradient estimation.
