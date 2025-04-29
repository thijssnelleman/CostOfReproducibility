
## Fine-grained Prediction of Political Leaning on Social Media with Unsupervised Deep Learning
Tiziano Fagni, Stefano Cresci
Keywords: 
JAIR/2022/Proceedings/13112 - Fine-grained Prediction of Political Leaning on Social Media with Unsupervised Deep Learning.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors state a lot of methods used from Sklearn in section 5 with a direct link. They also state they use word2vec from the gensim library. These give very good starting points. Overviews are given in figure 1/3/4. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors publish their data online and provide a link in footnote 5 (https://zenodo.org/records/5793346). The data collection strategy is stated in section 3 in great detail, and provide visualisations of the data in figure 2 and statistics in table 1.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

Architecture given in figure 4 (a bit high level). A lot of hyperparameter details are not clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors measure P/R/F1 and present confusion matrices. Data split stated in 3.2 and is given in the data link. It is not always clear on which split the results are presented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Requries expertise on unsupervised deep learning.
