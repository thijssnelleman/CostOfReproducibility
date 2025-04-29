
## MMD Aggregated Two-Sample Test
Antonin Schrab, Ilmun Kim, Mélisande Albert, Béatrice Laurent, Benjamin Guedj, Arthur Gretton
Keywords: 
JMLR/2023/Proceedings/211289 - MMD Aggregated Two-Sample Test.pdf
Project URL: https://github.com/antoninschrab/mmdagg-paper

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website and in the introduction (https://github.com/antoninschrab/mmdagg-paper). In the readme they state details on the method, installation requirements and instructions, how to reproduce the experiments with explanations and links, how to download/generate the datasets, and practical details. Comments are very good. Structure can use an index. Pseudo code in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors provide a dataset file in the implementation for MNIST and download links + generation instructions, citation given in the paper and description but statistics lacking. The authors also use CIFAR-10 and provide a citation but nothing else.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state the algorithm in speudo code 1. There they list the required inputs. The values are stated in the text of the experiment but no acquisition method. No structured overview, neither in the code as experiments.py is not very easy to read.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

Table 1 has results repeated 5 times and averaged. Other results are averaged over 500 repitions, metrics are power laplace kernel and power but are not explained. No data split applicable.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on kernel methods.
