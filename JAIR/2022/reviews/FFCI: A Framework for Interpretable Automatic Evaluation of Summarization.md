
## FFCI: A Framework for Interpretable Automatic Evaluation of Summarization
Fajri Koto, Timothy Baldwin, Jey Han Lau
Keywords: 
JAIR/2022/Proceedings/13167 - FFCI: A Framework for Interpretable Automatic Evaluation of Summarization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide a link to their implementation in the introduction (https://github.com/fajri91/ffci). In the readme they state a description on the method and where to find the data. There is no code.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors provide datasets in the implementation link. They use XSUM and CNN/DailyMail datasets and for models PG, TCONV, TRANS2S, BERT to do data labellings. The datasets are published in the implementation. The authors use Amazon Mechanical turk for dataset construction and describe/visualise the process in 5.2. Statistics in table 5. Asside from the constructed dataset they also use XSUM in general.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[6]

The authors use pretrained models. However they also discuss training/development/test data in section 5 and informally state a few hyperparameters. It is not completely clear what corresponds with what experiment and how the values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors discuss metrics in 3.3. and state them in 5.3. with citations/direct links. They measure averaged pearson correlation score over 5 runs based on five training data variants. They also measure this over layers. In general everything is well documented but it will require some experience in the NLP field to set it up.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on NLP.
