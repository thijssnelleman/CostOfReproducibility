
## Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation
Kun Yuan, vinkle srivastav, Nassir Navab, Nicolas Padoy
Keywords: 
NeurIPS/2024/Proceedings/92928 - Procedure-Aware Surgical Video-language Pretraining with Hierarchical Knowledge Augmentation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors publish their code online (https://github.com/CAMMA-public/PeskaVLP). In the readme they state a description on the method and where it was published including two references regarding the development acknowledgements, installation requirements, how to prepare the data and where to download it from, how to configure the method before running and how to train. The code has okay comments. The directory structure is huge and needs an index. In figure 1, 2 and 3 the authors illustrate the method. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(4/4)

The authors state the data sets used in section 4. The SVL data set is cited, as well as the evaluation data sets Cholec80, autolaparo, multibypass. Descriptions on these datasets are given in appendix A. Direct links are provided in the implementation for 2. Statistics are few.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide cofniguration files for the experiments in the implementation. The values for the experiments are summarised in the text as well in sec 4. No acquisition specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Data splits are given in the implementation. The authors report accuracy and F1 scores as metrics. The evaluation strategy is zero shot and few/full shot which is described in sec 4. The results are single model/run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on medical data / tasks and CV + NLP.
