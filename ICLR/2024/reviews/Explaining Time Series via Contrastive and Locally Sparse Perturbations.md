## Explaining Time Series via Contrastive and Locally Sparse Perturbations
Zichuan Liu, Yingying ZHANG, Tianchun Wang, Zefan Wang, Dongsheng Luo, Mengnan Du, Min Wu, Yi Wang, Chunlin Chen, Lunting Fan, Qingsong Wen
Keywords: 
ICLR/2024/Proceedings/17742 - Explaining Time Series via Contrastive and Locally Sparse Perturbations.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/zichuan-liu/ContraLSP). Readme has install instructions, how to run with toy data, and how to run the code to reproduce the experiments. Code has good comments. Structure is huge and needs an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use synthetic data called: , parse white-box regressors, Switch-Feature and State, MIMIC-III dataset. Described and cited in 5.1-5.3. Code provided but no link to MIMIC.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

HPs summarised in table 6 of appendix D per dataset. Not all acquisition clarified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

Authors measure AUP ↑ AUR ↑ Im/104 ↑ Sm/102 as well as ACC ↓ CE ↑ SUFF∗102 ↓ COMP∗102 ↑ (described in sec 5) reported using mean ± std of 5 repetitions. No split specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
