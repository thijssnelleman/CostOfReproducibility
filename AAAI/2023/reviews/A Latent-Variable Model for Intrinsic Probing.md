
## A Latent-Variable Model for Intrinsic Probing
Karolina Stańczak, Lucas Torroba Hennigen, Adina Williams, Ryan Cotterell, Isabelle Augenstein
Keywords: SNLP: Interpretability & Analysis of NLP Models, SNLP: Machine Translation & Multilinguality
AAAI/2023/Proceedings/26593 - A Latent-Variable Model for Intrinsic Probing.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation 'to replicate our experiments' (https://github.com/copenlu/flexible-probing). The readme has details on installing their implementation, how to generate the data (and where to download its source from with a link), and some details on how you can run the code. The code seems to have a decent amount of comments, and there are quite some notes on the implementation in the paper as well. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors provide a direct link to download the data set in the implementation. There is a small discription on the data in the experimental set up and how it was used for the experiment, and they refer to a previous work for more details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors clearly state they hyperparameters in 4.4. They state these values were confirmed by conducting a grid search. It is not stated how large this grid was (e.g. how many configurations were tried).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors discuss the metrics used in great length and provide citations for further details. The training procedure is specified in 4.4. The complete experimental set up is discussed in 4 with citations provided.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The paper requires a deep understanding of NLP and intrinsic probing, although clear documentation on it is provided in this paper. However, extra sources will be needed to grasp and reproduce the method in full.
