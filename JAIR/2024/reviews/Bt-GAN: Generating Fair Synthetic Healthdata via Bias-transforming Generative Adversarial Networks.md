
## Bt-GAN: Generating Fair Synthetic Healthdata via Bias-transforming Generative Adversarial Networks
Resmi Ramachandranpillai, Md Fahim Sikder, David Bergström, Fredrik Heintz
Keywords: 
JAIR/2024/Proceedings/15317 - Bt-GAN: Generating Fair Synthetic Healthdata via Bias-transforming Generative Adversarial Networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The implementation details are stated in Appendix C, and state they use PyTorch as framework. No other details.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

In section 8 the authors use the MIMIC-III dataset and provide a brief description and a citation, but no link, some statistics in the appendix. In section 9 the authors use the Adult an compas dataset, provide direct links but few statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the architecture in table 9. In appendix C some Hp values are also stated. No acquisition given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors measure accuracy, F1, AUROC, Discriminative score, JSD, precision and recall, Authenticity and Context FID but not all metrics are clear/standard/explained. Data split is stated in appendix C. It is not always clear against which data split is being evaluated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on fair data generation.
