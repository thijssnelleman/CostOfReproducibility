
## Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion
Ishaan Rawal, Alexander Matyasko, Shantanu Jaiswal, Basura Fernando, Cheston Tan
Keywords: 
ICML/2024/Proceedings/33856 - Dissecting Multimodality in VideoQA Transformer Models by Impairing Modality Fusion.pdf
Project URL: https://dissect-videoqa.github.io

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/israwal/dissect-videoqa). The readme has a short index on the repository. They explain how the data for their work was curated from another dataset. The authors present an analysis/metric ('probe') for which they provide a notebook. The codebase is small and easy to overseee, and there is a decent amount of comments. There are no installation instructions, but does provide run examples. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors provide a direct link to the source dataset. They use this to produce their own, for which they share the code and instructions on how it was curated. The result of this is also present. Furthermore, they use four benchmark datasets for which they provide citations but no links/descriptions/explanations. There is also a simulation dataset used which is completely clarified in appendix A.5.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the HPs of the models used from previous works in table 14. Their own method is parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors present experiments with single model runs over various datasets. The metrics are accuracy. Their method operated for the non synthetic experiment on inference time only, thus train-test splits are not applicable. For the synthetic data, they explain all details in appendix A.5.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on CV/NLP/Transformers. 
