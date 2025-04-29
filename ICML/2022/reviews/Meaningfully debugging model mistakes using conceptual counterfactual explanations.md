
## Meaningfully debugging model mistakes using conceptual counterfactual explanations
Abubakar Abid, Mert Yuksekgonul, James Zou
Keywords: 
ICML/2022/Proceedings/16721 - Meaningfully debugging model mistakes using conceptual counterfactual explanations.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/mertyg/debug-mistakes-cce). In the readme they show an overview of the method and how to run the code with various examples. There are no installation instructions. The code has decent comments. Pseudo code is given in algorithm 1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors use the MetaDataset and cite it + description on how it was used, and citations for Fitzpatrick17k, ISIC, NIH, SHC with brief descriptions. The authors also used the Broden dataset. A concept bankl dataset is given in the implementation. Only a direct link is given for fitzpatrick17k in the appendix A.5.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are stated in algorithm 1. The values for each experiment are stated in 3.2. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use mean precision and median rank for evaluation, which are averaged over 20 scenarios. The authors specify on the data set subset they evaluate per experiment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on counter factual explanation.
