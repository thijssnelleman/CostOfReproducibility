
## Estimation and inference on high-dimensional individualized treatment rule in observational data using split-and-pooled de-correlated score
Muxuan Liang, Young-Geun Choi, Yang Ning, Maureen A Smith, Ying-Qi Zhao
Keywords: 
JMLR/2022/Proceedings/210993 - Estimation and inference on high-dimensional individualized treatment rule in observational data using split-and-pooled de-correlated score.pdf
Project URL: https://github.com/muxuanliang/ITRInference.git

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation on the JMLR website as well as in section 4 (https://github.com/muxuanliang/ITRInference). In the readme they describe the package and provide an example. No installation instructions. Comments are good. Structure is simple.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(1/1)

The authors conduct simulations for their experiments. the generation formulae are stated in section 4 but it is quite information dense. Parameters and their values are stated. Its not clear if the code for it is available in the implementation. In section 5 the authors use a dataset regarding diabetes and provide a description and statistics. No citation or link provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[7]

The authors describe the paramters of their method in the code and in algorithm 1-3. Some of the values are given in the text of section 4, but a full overview is missing and the values are not always clear. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the data split in section 5. The authors measure the power and covera of non-zero coefficients (not formally defined). The results are presented in table 1 with mean and standard deviations on the value functions. Procedure is repeated 100 times with different seeds to produce the population. In the graphs the averages are presented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on high dimensional inference.
