
## Knowledge Enhanced Representation Learning for Drug Discovery
Thanh Lam Hoang, Marco Luca Sbodio, Marcos Martinez Galindo, Mykhaylo Zayats, Raul Fernandez-Diaz, Victor Valls, Gabriele Picco, Cesar Berrospi, Vanessa Lopez
Keywords: KRR: Other Foundations of Knowledge Representation & Reasoning, ML: Multimodal Learning
AAAI/2024/Proceedings/29757 - Knowledge Enhanced Representation Learning for Drug Discovery.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/IBM/otter-knowledge). There is a very extenstive explanation in the readme, rich with images, tables, links to other resources, models descriptions, installation instructions, details on how to run the code regarding inference, training the benchmarks models, running ensemble learning and some file structure descriptions. The code is generally well structured but rather large, and could use more comments. The paper provides a work flow diagram.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(7/7)

The authors use 7 data sets, give a citation on each one with description and statistics, and discuss data preprocessing methods. A table with more information on five of these data sets is provided including their accessibility (all of which are open). There are links provided on the implementation docs on where to find these data sets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The paper states GNN hp's are detailed in the appendix which doesn't exist (AAAI limitations). The authors provide options in the implementation docs on how to feed the program its hyperparameters, perhaps they can be extracted from there. No details on how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

The general workflow of the method is well documented with important notes on the experimental procedure regarding training/testing splits, but some specifications would have to be extracted with some effort. The metrics are only briefly noted in the table 2 caption.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

The method is well worded and very well documented, asside from some missing information regarding config/experiments, which could possibly still be extracted. However, the method is qutie complex and requires some previous understanding of the problem, GNNs and knowledge graphs to fully reproduce it.
