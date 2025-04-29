
## VideoPoet: A Large Language Model for Zero-Shot Video Generation
Dan Kondratyuk, Lijun Yu, Xiuye Gu, Jose Lezama, Jonathan Huang, Grant Schindler, Rachel Hornung, Vighnesh N Birodkar, Jimmy Yan, Ming-Chang Chiu, Krishna Somandepalli, Hassan Akbari, Yair Alon, Yong Cheng, Joshua V Dillon, Agrim Gupta, Meera Hahn, Anja Hauth, David Hendon, Alonso Martinez, David Minnen, Mikhail Sirotenko, Kihyuk Sohn, Xuan Yang, Hartwig Adam, Ming-Hsuan Yang, Irfan Essa, Huisheng Wang, David Ross, Bryan Seybold, Lu Jiang
Keywords:
Award: Best Paper
ICML/2024/Proceedings/2458 - VideoPoet: A Large Language Model for Zero-Shot Video Generation.pdf
Project URL: https://sites.research.google/videopoet/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide a link to their project page which contains many examples on the method. A layout of their method is presented in figure 2, and an architecture overview in figure 3. The authors give some implementation details in appendix A.5 but practical details (such as libraries/frameworks) are not given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[6]

(5/6)

The authors state the dataset in section 5.1 with some high level statistics and a note on how it was filtered for training which is seemingly private. Furthermore, the authors state five benchmark datasets they use for evaluation for which they provide citations and briefy descriptions and very few or no statistics. No direct links provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[8]

The authors state the grandient descent method using in 4.2. In 5.2. the learning rate and batch size is mentioned and stated these are for all experiments. No overview on the HP space is given. No acquisition method is specified (except that the method wasn't finetuned per task). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the evaluation metrics in appendix A.5 per task with citations but no full explanations. The authors state which dataset is used for training and which for evaluation. The results are per model (single run).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[9]

Requires expertise on CV, including a lot of practical experience due to the size of the presented method (loads of parameters and tasks applicability). 
