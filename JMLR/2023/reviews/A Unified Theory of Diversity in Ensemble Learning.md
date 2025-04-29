
## A Unified Theory of Diversity in Ensemble Learning
Danny Wood, Tingting Mu, Andrew M. Webb, Henry W. J. Reeve, Mikel Luján, Gavin Brown
Keywords: 
JMLR/2023/Proceedings/230041 - A Unified Theory of Diversity in Ensemble Learning.pdf
Project URL: https://github.com/EchoStatements/Decompose

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website (https://github.com/EchoStatements/Decompose) and in the conclusion as well. In the readme they state hwat the library contains, how to install, how to run with 3 examples. Code has good comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

There is a download script in the implementation for Phoneme, Landsat, Spambase, SouthGermanCredit and MNIST but most these are only used in the appendix (except for MNIST). In section 4.3. the authors present results on California Housing Data, which the authors do not provide any details on but is automatically downloaded in their code through sklearn. They also use a synthetic dataset on which they provide a citation on and a generator for in the code.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors method is parameter free. They provide notebooks per experiment with all the values regarding their experiments for the non-parameter free methods used. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure (squared) error and cross-entropy as well as loss. Formulas given where applicable. Results are over ensemble sizes, which is aggregated using ensemble techniques. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise on ensembling.
