
## Complex Query Answering on Eventuality Knowledge Graph with Implicit Logical Constraints
Jiaxin Bai, Xin Liu, Weiqi Wang, Chen Luo, Yangqiu Song
Keywords: 
NeurIPS/2023/Proceedings/70360 - Complex Query Answering on Eventuality Knowledge Graph with Implicit Logical Constraints.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors share a link to their implementation (https://github.com/HKUST-KnowComp/CEQA). In the readme they state where to download the data and how to sample it and how to do query encoding with their code. Installation instructions not given. The code can use more comments. Structure is not too complex (a bit unorgainsed maybe with all the .sh files here and there).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors provide a download link to a subset from ASER2.1 in the implementation (original as well + subsampling code given). The sampling is explained in detail but descriptions/statistics on the dataset are lacking.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state they conduct hyper-parameter selection on the validation set in 4.2. They state they select these using grid search and the grids are provided in 4.3. Structured overview missing as well as selected value per experiment.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Data split given in sec 4. The authors use Hit@k and MRR as metrics and explain them in sec 4.2 and state they report them on the validation/test set. Each experiment is repeated three times and they report the average. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on knowledge graphs.
