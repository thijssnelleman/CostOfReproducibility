
## Correct for Whom? Subjectivity and the Evaluation of Personalized Image Aesthetics Assessment Models
Samuel Goree, Weslie Khoo, David J. Crandall
Keywords: PEAI: Philosophical Foundations of AI, CV: Image and Video Retrieval, APP: Art/Music/Creativity, APP: Humanities & Computational Social Science, PEAI: Morality and Value-Based AI, PEAI: Societal Impact of AI
AAAI/2023/Proceedings/26395 - Correct for Whom? Subjectivity and the Evaluation of Personalized Image Aesthetics Assessment Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors mainly evaluate and re-label a data set in this work. However, there is also an experiment of retraining a model based on previous work to their re-labelled data set. This implementation is missing and would be welcome as it should be part of reproducing the method. However, as the results of this model is only a small part of the problem, and the suggested method (SVM) is relatively easy to apply, only a low cost is awarded here as all other parts of the method do not require implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors review and re-label a public data set. Their version is publicly available and url is given (http://vision.soic.indiana.edu/pr-aadb/). Extensive details are provided on the new data set.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Not applicable, perhaps asside from the applied SVM which is only a very small part of this work.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The method mainly describes a data analysis which is well explained. There is a small experiment regarding SVM training which has clear experimental details.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[1]

The method is quite accesible but requires some previous understanding about dataset statistics, biases and their metrics/evaluations.
