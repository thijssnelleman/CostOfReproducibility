
## Overlooked Implications of the Reconstruction Loss for VAE Disentanglement
Nathan Michlo, Richard Klein, Steven James
Keywords: Machine Learning: ML: Representation learning, Machine Learning: ML: Autoencoders, Machine Learning: ML: Unsupervised learning, Machine Learning: ML: Explainable/Interpretable machine learning
IJCAI/2023/Proceedings/0453 - Overlooked Implications of the Reconstruction Loss for VAE Disentanglement.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors link to a repository called Disent (https://github.com/nmichlo/disent) and state that this is a contribution of the work. It is a bit confusing though because the citing paper in the readme differs from this paper. It is a 'PyTorch disentagelement framework with common models metrics and datasets'. As a framework, it checks all the boxes of understandble code, with full documentation, extensive readme, and extensive comments. However, the code actually used to produce the experiments of the paper is not directly shared. Thus still some effort is to be done, but with the extensive framework this should be very much aleviated.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors use synthetic/generated data, and state the procedure in section 4.1 with an example in figure 2. The code for this can be found in their linked framework.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors perform a hyper-parameter grid search, and state they perform this on various HPs, refering to the extended paper under footnote 1 for further details. Table A4 provides all needed information regarding the search and budgets.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state each experiment is repeated five times. They state their experimental setup in 5.2. Here they state the metrics used and values used for their methods. Details on training/test set are not completely clear but could be irrelevant due to synthetic data. Requires some expertise and effort to verify.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise with VAE and disentanglement.
