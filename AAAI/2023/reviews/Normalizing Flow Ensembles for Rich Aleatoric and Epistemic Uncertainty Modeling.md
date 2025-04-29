
## Normalizing Flow Ensembles for Rich Aleatoric and Epistemic Uncertainty Modeling
Lucas Berry, David Meger
Keywords: ML: Calibration & Uncertainty Quantification, ML: Active Learning, ML: Ensemble Methods, ML: Multimodal Learning, ML: Probabilistic Methods
AAAI/2023/Proceedings/25834 - Normalizing Flow Ensembles for Rich Aleatoric and Epistemic Uncertainty Modeling.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide their implementation source (https://github.com/nwaftp23/nflows_epistemic). There the authors have a short readme regarding requirements installation. The usage section is empty, the Bibtex section is 'coming soon'. There are a lot of different files and very few comments in them, making the structure a bit hard to follow. As the there are no execute instructions the process would also have to be reverse engineerd. The paper has a general diagram of the method, but is not extremely detailed. In general the implementation could use better documentation, as a lot is left to independent investigators to figure out.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(5/5)

The authors use 5 simulated environments, which are publicly available and some slightly modified which are available in the implementation documentation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

For the hyperparameter documentation the authors refer in the paper to the implementation. Due to the unexplained structure and lack of documentation of the repository in general, this will take some effort to extract this information. No note is given how these values are supposedly acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors acquire model trajectories on the environments and evaluate the discussed metrics. It is a bit difficult to directly assess how this process is done and would have to be extracted from the implementation as well.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The evaluation type of this paper are highly specific and complex concepts. The authors refer to other source material which definetily helps. In general the expertise required is quite high, which is not for the lack of documentation by the authors.
