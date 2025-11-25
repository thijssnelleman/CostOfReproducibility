## Distributed Representations of Sentences and Documents
Quoc Le, Tomas Mikolov 
Keywords: 
extra_reviews/2014/Proceedings/Distributed Representations of Sentences and Documents.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[8]

The authors provide a link for the word2vec implementation of their previous work. However, the implementation of their own method is not provided. Overview of the method in figure 1, 2 and 3. The provided implementation could serve as a starting point, but not much more.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/3)

Stanford Sentiment Treebank Dataset (cited, described and linked), IMDB dataset (cited, described and linked), and a third private dataset which is described with good details on acquisition strategy and size including examples but the resources required to acquire this dataset may be fairly limited (access to search engine data).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[10]

The authors select the hyperparameter values on the validation set. Budget, strategy, and values are not provided. On the architecture there is a note for the IMDB dataset. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors split the private dataset 80/10/10 tvt, for the other datasets they use the static split. They measure the error rates on the task. Results are single run.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
