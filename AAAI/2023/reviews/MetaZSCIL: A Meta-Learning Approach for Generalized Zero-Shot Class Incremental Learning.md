
## MetaZSCIL: A Meta-Learning Approach for Generalized Zero-Shot Class Incremental Learning
Yanan Wu, Tengfei Liang, Songhe Feng, Yi Jin, Gengyu Lyu, Haojun Fei, Yang Wang
Keywords: ML: Multi-Instance/Multi-View Learning, CV: Image and Video Retrieval
AAAI/2023/Proceedings/26238 - MetaZSCIL: A Meta-Learning Approach for Generalized Zero-Shot Class Incremental Learning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a link to their implementation. There is a section on implementation details which is actually mainly about hyperparameters. A large overview of them proposed method is given and some pseudo code. No other details are provided on the implementation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(5/5)

The authors use five benchmark data sets, provide citations on them and share key statistics/meta information on them. No direct link is given, but enough information that it should be able to find it with little effort. The lack of implementation however means potential pre-processing will have to be inferred from the paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors provide the hyperparameter values of their method, per data set. No details are given on how these are acquired. It is unclear if the full hyperparameter space is covered with the values given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide details on the data sampling, they apply zero shot metrics and explain their meaning, and compare their evaluation protocol to previous work and where it differs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a very good understanding of meta learning and zero shot learning, combined with a computer vision task. As the authors state they consider a new problem setting, this prior knowledge will be required to fully grasp their setting. The lack of implementation makes this somewhat more difficult as there is less examples/documentation to work with and independent investigators cannot rely on previous/comparable work for 'inspiration'.
