
## ECG-QA: A Comprehensive Question Answering Dataset Combined With Electrocardiogram
Jungwoo Oh, Gyubok Lee, Seongsu Bae, Joon-myoung Kwon, Edward Choi
Keywords: 
NeurIPS/2023/Proceedings/73554 - ECG-QA: A Comprehensive Question Answering Dataset Combined With Electrocardiogram.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/Jwoo5/ecg-qa). In the readme they state updates, release notes, demonstrations with a link, describe the data set and its attributes, the structure of the data, how to use, a quick start to run experiments with various examples, and contact info. The code has few comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

Footnote one gives a link to the dataset the authors present in the paper (the implementation). They describe the data there with loads of details. The data set construction is detailed in sec 3. and more details are given in the appendix. Statistics are given in appendix B.4.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparmater values are detailed in appendix C.1.1. in table 11. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state and describe the metrics in 4.1. Dataset split is given in the data set (static) and described in appendix table 9. The authors evaluate on the test set. The aggregation is specified in the captions. They report the values with 95% confidence over three random seeds. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requries expertise on QA datasets (NLP) and electrocardiogram data.
