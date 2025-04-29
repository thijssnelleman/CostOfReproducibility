
## BiE: Bi-Exponent Block Floating-Point for Large Language Models Quantization
Lancheng Zou, Wenqian Zhao, Shuo Yin, Chen Bai, Qi Sun, Bei Yu
Keywords: 
ICML/2024/Proceedings/34619 - BiE: Bi-Exponent Block Floating-Point for Large Language Models Quantization.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors do not share their implementation. However, a design overview is given in figure 4 and 5, implementation details are specified in 3.3 including tools used, statements on what exactly was implemented, libraries used in 4.1. The authors also directly link/cite another work on which they based their evaluation code in 4.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(8/8)

The authors use a public data set and present a direct link to it. The authors use 7 datasets for evaluation for which they present a citation but no direct link. No statistics given, only very brief descriptions. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors detail the implementation settings in 4.1. They measure different configurations of their method in table 2 and 3. Other than that parameters do not apply. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors evaluate the method on various LLMs. They measure 'performance' in table 3 and 'perplexity' in table 4/5 but these are not explained. The results are single models/runs. The benchmark datasets are stated in 4.1.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on quantization.
