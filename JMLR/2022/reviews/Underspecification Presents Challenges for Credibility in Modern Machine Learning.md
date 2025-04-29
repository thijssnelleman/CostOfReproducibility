
## Underspecification Presents Challenges for Credibility in Modern Machine Learning
Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew D. Hoffman, Farhad Hormozdiari, Neil Houlsby, Shaobo Hou, Ghassen Jerfel, Alan Karthikesalingam, Mario Lucic, Yian Ma, Cory McLean, Diana Mincu, Akinori Mitani, Andrea Montanari, Zachary Nado, Vivek Natarajan, Christopher Nielson, Thomas F. Osborne, Rajiv Raman, Kim Ramasamy, Rory Sayres, Jessica Schrouff, Martin Seneviratne, Shannon Sequeira, Harini Suresh, Victor Veitch, Max Vladymyrov, Xuezhi Wang, Kellie Webster, Steve Yadlowsky, Taedong Yun, Xiaohua Zhai, D. Sculley
Keywords: 
JMLR/2022/Proceedings/201335 - Underspecification Presents Challenges for Credibility in Modern Machine Learning.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

Not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/5)

In sectio n5 the authors use ImageNet (citation), ObjectNet (citation), but do not provide any details on the datasets. In section 6.2 they use EyePACS dataset (no citation provided and it seems to be private). In section 7 the authors use wikipedia and bookcorpus. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors evaluate specified pipelines from other methods to study them but details are a bit vague sometimes, configurations are not focussed on getting 'best' results so acquisition not as relevant. Structured overview is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure accuracy as mean and standard dev. Dataset splits are specified an on which they report the values. Population comes from ensembles. For the other experiments everything seems to be well specified too.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries epxertise on general ML methods, data drift / overfitting and applications of ML (pipelines).
