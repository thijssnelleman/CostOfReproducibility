
## PECOS: Prediction for Enormous and Correlated Output Spaces
Hsiang-Fu Yu, Kai Zhong, Jiong Zhang, Wei-Cheng Chang, Inderjit S. Dhillon
Keywords: 
JMLR/2022/Proceedings/210085 - PECOS: Prediction for Enormous and Correlated Output Spaces.pdf
Project URL: https://libpecos.org/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide a link on JMLR website for their project (https://libpecos.org/) but this does not resolve. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/6)

The authors provide a download link for downloading the six benchmark datasets. Statistics are provided on each in table 2. No descriptions given.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors conduct an ablation study on parameter T, B and D in table 6 (grid) and define them in section 3. They are also specified for the experiments before but where the values exactly come from is not completely clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure Prec@b, Recall@b and provide formulas on them also time in seconds. The authors refer for datasplits to a previous work and based on the statistics table 2 they seem to be static but the actual split is not given. Results are single run and presented on the train / test set (varies per table).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on extreme multi-label text classifcation.
