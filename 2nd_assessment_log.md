# Log regarding 2nd assessment of papers

### 01-04-2025

#### Review of JD

Regarding: 
- SKDBERT: Compressing BERT via Stochastic Knowledge Distillation - AAAI 2023

##### Questions

Q: If the implementation is not provided in my opinion, I can increase the cost with up to 4. Why would it be less?
A: If there is some context in which parts of the implementation is given, but not the exact code regarding the experiments. ("We publish our method in library Y", but not "Our code for the paper is available at X").

Q: For the strategy of Exerpimental Setup, does multiple seeds count as a strategy?
A: Yes, this is considered multiple runs.

Q: Is the expertise evaluated on a scale from 1-10 too? Is 1 easy and 10 difficult?
A: Yes, this was not clear in the guidelines. 1 means you have to read almost nothing or nothing beside the paper to reproduce it, 10 means you have to either have a lot of expertise or rely alot on other sources asside from the provided documentation to reproduce.


### 02-04-2025

#### Review of NK 

Regarding:

- FedSoft: Soft Clustered Federated Learning with Proximal Local Updating
- TFLOP: Table Structure Recognition Framework with Layout Pointer Mechanism
- Scalable Optimal Margin Distribution Machine

##### Questions

Q: Am I allowed to look at the contents of the papers the authors cite?
A: No, this is outside the domain of this work. We consider the paper itself and any direct links as long as it belongs to this paper.

Q: Am I allowed to look at appendices posted online?
A: Yes this is fine, if its the appendix that belongs to this paper and not a different paper.

Q: What is the meaning of the sentence in Data section 2nd paragraph? "For each dataset that is named and has a description, citation, statistics and a direct link to where it can be found. If you recognise the dataset, feel free to use that information regarding public/private data"
A: This was not phrases clearly. Updated to: "For each dataset that is used, check that it has a description, citation, statistics and a direct link to where it can be found. If you recognise the dataset, feel free to use this information regarding public/private data."

Q: If they use data generators is it private data?
A: The second paragraph in Data section checklist is regarding synthetic data.

Q: Do I evaluate the expertise from 1-10 as well?
A: Yes, 1 being accesible and 10 requiring a lot of expertise. Added a single sentence to the guideline to clarify.

Q: Is the last add five in data set on top of everything else?
A: Yes, it is additional cost.


#### Review of HS

Regarding:

- STEM: Unleashing the Power of Embeddings for Multi-Task Recommendation
- GOCPT: Generalized Online Canonical Polyadic Tensor Factorization and Completion
- Randomized Confidence Bounds for Stochastic Partial Monitoring

Q: The data set description is any kind of description?
A: Yes, as long as you feel like this description gives you enough information to understand the dataset and the task.

Q: If I know the dataset do the statistic still matter?
A: Yes this is still important, only use your knowledge on the datasets when it comes to deciding public versus private.

Q: What does 'informal in the text' mean?
A: The summary is unstructured data (written in text form), whereas structured means any kind of table or code (structured) representation.

Q: How do I aggregate over experiments?
A: Weighted averaging, like the datasets. 

### 07-04-2025

#### Review of JD

Regarding: 
- Entropy Estimation via Normalizing Flow 

### 08-04-2025

#### Review of AJ

Regarding:
- On-Demand Sampling: Learning Optimally from Multiple Distributions
- Towards Continual Learning Desiderata via HSIC-Bottleneck Orthogonalization and Equiangular Embedding

Q: What should I consider as part of the documentation?
A: Anything directly posted on the conference/journal website and things that are directly linked there (such as openreview) or is directly linked in the paper. The moment that you a 'google search' for example to get information it is documentation outside the scope of the paper: It needs to be selfcontained.

### 09-04-2025

#### Review of HD

Regarding:
- Wide Two-Layer Networks can Learn from Adversarial Perturbations
- DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models
- Graph Neural Networks are Dynamic Programmers

Q: Should I follow the links to the datasets the authors give?
A: No, we assume the information the authors present us with is correct and the documentation that is not produced/provided by the authors is out of scope for the evaluation.

#### Review of AJ

Regarding:
- Disentangling Disease-related Representation from Obscure for Disease Prediction


### 10-04-2025

#### Review of BR

Regarding:
- Reversible and irreversible bracket-based dynamics for deep graph neural networks
- The Phenomenon of Policy Churn

Q: Why is the example II configuration still 3? Everything seems to be given.
A: This is a lack of details in the screenshots: In this case they documented a lot of information, however not all values were given per experiment.

Q: What do I do if only a part of the code has been given regarding the experiments?
A: Check that the code regarding the main contribution is there, this is the most important part. If its missing parts of specific experiments, its less important. However if you think this hinders the re-implementation of the method you can still increase the score by 1 (or more) for example.

Q: Is variance the only measure of distrubition allowed in the results?
A: This was a typo in the guidelines. Has been fixed.


#### Review of WS

Regarding:
- On Generalized Degree Fairness in Graph Neural Networks
- Better Embedding and More Shots for Few-shot Learning
- Tractable Dendritic RNNs for Reconstructing Nonlinear Dynamical Systems

Q: Am I allowed to use the appendix if its not posted on the publication website?
A: No, then its considered out of scope for this work.

### 14-10-2025

#### Review of KK

Regarding:
- Community detection in sparse latent space models
- On Sufficient Graphical Models
- On Unbalanced Optimal Transport: Gradient Methods, Sparsity and Approximation Error

Q: I don't have a lot of expertise in this subfield. Does that matter?
A: No, not persay, simply have a look if the subfields specifics are explained, and if not raise the cost accordingly as it is a required knowledge/expertise for the independent investigators.

Q: What do you mean with 'enough' data set statistics?
A: In general you try to evaluate if there is enough statistical information present, s.t. you can explain/defend using another dataset in its stead and 'enough' varies per dataset.

#### Review of JD

Regarding:
- Lazy Agents: A New Perspective on Solving Sparse Reward Problem in Multi-agent Reinforcement Learning

### 17-04-2025

#### Review of AB

Regarding:
- DANets: Deep Abstract Networks for Tabular Data Classification and Regression

### 23-04-2025

#### Review of JDe

Regarding:
- Approximate Counting of Linear Extensions in Practice

Q: The authors compare CPU and GPU algorithms, and this can complicate the experiment result if I were to use different systems, should I use this for my evaluation?
A: Not persay, the focus should be here on whether the procedure itself is well documented enough to set up another one not one getting 'the same results'.

Q: They do not provide a link for a dataset, should I Google it?
A: No, we assume based on what the authors imply whether data is public or private.
