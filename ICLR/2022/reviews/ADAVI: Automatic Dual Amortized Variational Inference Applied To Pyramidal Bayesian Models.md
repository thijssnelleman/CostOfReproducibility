## ADAVI: Automatic Dual Amortized Variational Inference Applied To Pyramidal Bayesian Models
Louis Rouillard, Demian Wassermann
Keywords: 
ICLR/2022/Proceedings/6309 - ADAVI: Automatic Dual Amortized Variational Inference Applied To Pyramidal Bayesian Models.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors state in the reproducibility statement a few details on the implementation, and do this extensively in appendix F.2., and that they release the code with the supplementary materials (https://openreview.net/attachment?id=CgIEctmcXx1&name=supplementary_material). The readme contains installation notes, an overview of the directory organization, how parts of the code work and what they are based on, and examples. They also include a long list of examples in said directory. Their code contains a lot of comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(2/3)

The authors use synthetic data for which they give the definition in 3.2 and the values in 3.3 and the generated files are present in the supplementary materials. The authors also conduct an analysis on a private dataset in 3.5 (HCP), on which a citation and some details are provided, in the appendix as well but more would be required for a full understanding. However, as they provide a citation to the paper supposedly containing this data, and clarification in the supplementary materials why this dataset is private, combined with the public data used, we weigh this relatively lowly as the authors cannot be expected to fully document a private dataset when this is not the subject of the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

There are some discussion regarding hyperparameter values in the appendix, but a structured overview seems to be missing. Acquisition also not always clear.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[2]

Authors measure ELBO (Not explained), Inference time in seconds and CPU amortization time in seconds. Results are over 20 or 5 random seeds and presented with median and standard deviation (ELBO) and a single sample for the time measurements.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
