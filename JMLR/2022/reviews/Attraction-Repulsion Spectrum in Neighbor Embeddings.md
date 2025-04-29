
## Attraction-Repulsion Spectrum in Neighbor Embeddings
Jan Niklas Böhm, Philipp Berens, Dmitry Kobak
Keywords: 
JMLR/2022/Proceedings/210055 - Attraction-Repulsion Spectrum in Neighbor Embeddings.pdf
Project URL: https://github.com/berenslab/ne-spectrum/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state a link to their implementation on the JMLR website as well as at the end of the introduction (https://github.com/berenslab/ne-spectrum/) and notes on it are given in 3.6. In the readme they state installation instructions, how to run the code, an overview of the structure of the code, explanation on some files an directoreis used at run time. Comments are good.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(7/7)

The authors use simulated data, as well as FMNIST, Kannada MNIST, Kuzushiji MNIST, single cell data, zebra fish embryo and mouse courtex on all of which they provide citations. No other details provided. Generator code provided in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The methods are parameter free except for an iteration maximum which the authors set to 750.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the embeddings over various unsupervised tasks.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on dimensionality reduction, clustering algorithms and unsupervised learning.
