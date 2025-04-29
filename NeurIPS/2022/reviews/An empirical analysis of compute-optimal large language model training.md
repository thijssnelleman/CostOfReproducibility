
## An empirical analysis of compute-optimal large language model training
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Thomas Hennigan, Eric Noland, Katherine Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karén Simonyan, Erich Elsen, Oriol Vinyals, Jack Rae, Laurent Sifre
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/372 - An empirical analysis of compute-optimal large language model training.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not provide their implementation. They do state the experiments have been conducted using JAX framework and Haiku library (citations/links provided). 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(12/14)

The authors construct a training dataset called MassiveText from 6 datasets. The authors use C4 and GitHub code datasets and cite them, but also MassiveWEb, Books, News and Wikipedia but for these no citations are given. High level statistics for all given in appendix A. No direct links and descriptions are shallow. It is unclear if the Books/News datasets are public. The authors evaluate the methods on 8 benchmark data sets and cite them and provide a brief description in appendix H.2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are summarised in table 3. More details given in appendix table A143. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors use seperate detasets for evaluation. The metrics (perplexity, accuracy) are stated in sec 4.2 but perplexity is not explained. The results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on LLMs.
