
## PerceptAnon: Exploring the Human Perception of Image Anonymization Beyond Pseudonymization for GDPR
Kartik Patwari, Chen-Nee Chuah, Lingjuan Lyu, Vivek Sharma
Keywords: 
ICML/2024/Proceedings/35031 - PerceptAnon: Exploring the Human Perception of Image Anonymization Beyond Pseudonymization for GDPR.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state the implementation and dataset is available online (https://github.com/SonyResearch/gdpr_perceptanon). However the link gives a 404 (26-03-2025). The authors state a few methods they used for parts of their implementation in 5.1, in 5.2 they state the framework used. A very high level overview is given in figure 5. There are a few technical details in the appendix.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(0/1)

The authors introduce their own curated dataset which is supposedly available online but the implementation link gives a 404. The acquisition method of the dataset is clearly specified including the annotation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

There are no specifications on hyperparameters regarding training. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors detail three training strategies in 5.1 includign train/test splits. They also detail the metrics in 5.1 with citations, and explain the acronyms in appendix F. There is no aggregation specified even though the strategies produce multiple folds.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with CV.
