
## Aspect-Based Sentiment Analysis with Explicit Sentiment Augmentations
Jihong Ouyang, Zhiyao Yang, Silong Liang, Bing Wang, Yimeng Wang, Ximing Li
Keywords: NLP: Sentiment Analysis, Stylistic Analysis, and Argument Mining
AAAI/2024/Proceedings/31478 - Aspect-Based Sentiment Analysis with Explicit Sentiment Augmentations.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors provide no implementation source in their paper. The authors provide a clear description of their method, both mathematical and graphical, and include an example of pseudo-code. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use a publicly available data set, cite the original authors and provide statistics on the data set.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide the values of key hyperparameters of their method for both tasks, but do not specify how these were acquired. The description is also relatively short for such complex methods and with the absence of implementation documentation this still may pose problems when attempting to compare configurations. Configurations for compared methods that were run by the authors themselves are completely absent.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors specify clearly their train and test set distributions. The authors do not explicitly state what method was used to accquire the results in their results table, but it seems to indicate that they are single run results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

The method requires a good understanding of text classification, and the loss / regularization methods presented are not straightforward to understand. This is not for a lack of trying by the authors however, and simply requires a high level of expertise to understand. Providing their implementation source would lower this threshold as it would provide independent investigators with more documentation/examples.
