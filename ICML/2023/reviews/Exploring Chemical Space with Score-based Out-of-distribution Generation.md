
## Exploring Chemical Space with Score-based Out-of-distribution Generation
Seul Lee, Jaehyeong Jo, Sung Ju Hwang
Keywords: 
ICML/2023/Proceedings/25071 - Exploring Chemical Space with Score-based Out-of-distribution Generation.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/SeulLee05/MOOD). I nthe readme they summarise the method, describe installation steps, how to run the data perperation, training, generation and evaluation and how to adapt the (hyper)parameters. The repository structure is a bit large but the naming scheme is done well making it overseeable. The code has very few comments. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors state a dataset used in 4.1 with citation. Its briefly described in appendix D4. The data is available in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors provide config files in the implementation. In the appendix the authors state they eperformed a grid search ofver the delta and r parameter as well as the NN architecture layers.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the metrics used with citation and description in 4.1. The test set acquisition is described in 4.1. as well. They generate 3000 molecules for evaluation. The results are over 5 runs and present the methods as mean and std dev.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires experience with molecule generation. 
