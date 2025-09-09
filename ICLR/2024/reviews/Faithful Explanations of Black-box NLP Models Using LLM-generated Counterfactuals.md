## Faithful Explanations of Black-box NLP Models Using LLM-generated Counterfactuals
Yair Gat, Nitay Calderon, Amir Feder, Alexander Chapanin, Amit Sharma, Roi Reichart
Keywords: 
ICLR/2024/Proceedings/18527 - Faithful Explanations of Black-box NLP Models Using LLM-generated Counterfactuals.pdf
Project URL: https://openreview.net/attachment?id=UMfcdRIotC&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their implementation in the reproducibility statement, but the repository only contains a readme with snippit of the paper abstract. The authors also provide code in the supplementary material (https://openreview.net/attachment?id=UMfcdRIotC&name=supplementary_material). There is no readme or comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

CEBaB, explained and cited in 4.1. no link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

Authors detail HPs in appendix G in text. There are also two config python files in the code. No motivation provided for most values.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

Data split given in 4.1. L2 Cos ND metrics are given over 24 'interventions', mean. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
