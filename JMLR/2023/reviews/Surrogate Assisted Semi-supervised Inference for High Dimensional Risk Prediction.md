
## Surrogate Assisted Semi-supervised Inference for High Dimensional Risk Prediction
Jue Hou, Zijian Guo, Tianxi Cai
Keywords: 
JMLR/2023/Proceedings/211075 - Surrogate Assisted Semi-supervised Inference for High Dimensional Risk Prediction.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

No implementation provided.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(2/2)

The authors do simulation studies in section 5. The authors state the generation process and formulas with parameters. No implementation. In section 6 they use a dataset called T2DM and describe it but no citations, statistics or links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

There is no clear defintion of the parameters (Table, pseudo code, or any overview). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors report AUC on an independent test set of 100 in table 1, but do not state how this set is acquired. In table 2 they evaluate Bias, ESE and rMSE over 500 labels. In table 3 the same but with 95% CI. In table 4 they present 10-fold cross validation results which they repeated 10 times, averaged. Figure 2 show CI as variation 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[10]

Requires expertise on high dimensional inference.
