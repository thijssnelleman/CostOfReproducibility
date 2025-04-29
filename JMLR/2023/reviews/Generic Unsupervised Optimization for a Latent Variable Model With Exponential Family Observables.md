
## Generic Unsupervised Optimization for a Latent Variable Model With Exponential Family Observables
Hamid Mousavi, Jakob Drefs, Florian Hirschberger, Jörg Lücke
Keywords: 
JMLR/2023/Proceedings/220359 - Generic Unsupervised Optimization for a Latent Variable Model With Exponential Family Observables.pdf
Project URL: https://github.com/tvlearn/evo

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state their implementation link on the JMLR website and footnote 4 (https://github.com/tvlearn/evo). In the readme they state a description on the repository, installation instructions, links to other packages for more information, and references. Code has good comments. There is a seperate directory with loads of examples. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use various distributions as synthetic data. They are explained in 7.1. and 7.1 and provided in the code. They also use datasets: CHiME (citation provided), visual data for which they provide the used images in figure 11. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

There are some notes of hyperparmaeters from other methods they use in their work and vary for example the H paramter of P-MCA in table 4. They do not present a method with own parameters.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

Experiments are repeated 3/100 times. Metrics are unclear in some tables. Aggregation is average. Data splits are not clear. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requires expertise on latent variable models and unsupervised learning.
