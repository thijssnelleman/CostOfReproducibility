
## Online Certification of Preference-Based Fairness for Personalized Recommender Systems
Virginie Do, Sam Corbett-Davies, Jamal Atif, Nicolas Usunier
Keywords: Machine Learning (ML)
Award: Outstanding Paper Award
AAAI/2022/Proceedings/733 - Online Certification of Preference-Based Fairness for Personalized Recommender Systems.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors link an extended version of the paper on arxiv on page 1. There they state in the appendix they use Python and link two GitHub repositories they used for the implementation and another in section 5. Pseudo code in algorithm 1/2. High level overview in figure 1. More details would be welcome but this does provide a starting point.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use the Last.fm dataset, whic they describe provide citation and direct link on but not a lot of statistics. They also use the MovieLens-1M dataset, which they also cite and provide descriptions on but no detailed statistics or direct link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state they conduct grid search using the train/validation set in appendix C.2. and also stated the used grids but not the selected values. Parameter values are stated in section 5 in text but no overview.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

Data split is stated in appendix C.2. Metrics are stated in section 4.2 and more formulae are stated in the appendices. Results are averaged over 100 trials in 5.2. It is not specified on which data split the results ar presented on.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries epxeritse on recommender systems and fairness.
