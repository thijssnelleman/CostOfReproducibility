
## Am I No Good? Towards Detecting Perceived Burdensomeness and Thwarted Belongingness from Suicide Notes
Soumitra Ghosh, Asif Ekbal, Pushpak Bhattacharyya
Keywords: Humans and AI: Computational Sustainability and Human Well-Being, Machine Learning: Attention Models, Machine Learning: Multi-task and Transfer Learning, Natural Language Processing: Resources and Evaluation, Natural Language Processing: Sentiment Analysis and Text Mining
IJCAI/2022/Proceedings/0704 - Am I No Good? Towards Detecting Perceived Burdensomeness and Thwarted Belongingness from Suicide Notes.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors show a detailed architecture in figure 1. The authors state some information in 5.2, including the framework used (TensorFlow), but no implementation is linked. Various other works that were used in the implementation are directly linked.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors use a benchmark dataset for their study, provide a citation on it, key statistics and a description. They expand the dataset with three tasks: Two annotations and a translation of the text. The annotator details are stated in 3.1. They provide a direct link to download their modified/expanded data set. Dataset statistics are discussed in 3.5. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state various hyperparameter values in 5.2, some of which seem to be empirical ("we chose"), but the authors also state grid search was also used to finetune on the validation set. The authors sate the architecture details as well. No budget on the acquisition is specified regarding the grid search, or which parameters were finetuned.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state they used 10-fold cross-validation for both data sets and macro-F1 as metric with an explanation. They also state this process was repeated five times and present the average to account for non-determinism.   

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires an understanding of NLP/LLMs.
