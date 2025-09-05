## Temporal Dependencies in Feature Importance for Time Series Prediction
Kin Kwan Leung, Clayton Rooke, Jonathan Smith, Saba Zuberi, Maksims Volkovs
Keywords: 
ICLR/2023/Proceedings/11463 - Temporal Dependencies in Feature Importance for Time Series Prediction.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the reproducibility statement (https://github.com/layer6ai-labs/WinIT). In the readme they state installation instructions, where to find the datasets including links and scripts, examples on how to run the code, and a notebook dedicated to rebuilding the tables and figures of the paper after running. The code has good comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/4)

The authors include three synthetic datasets (described in 5.1 with citations) in their implementation repository and link the code used to generate it. They also note for the MIMIC-III, and link the documentation, that it is private and how to acquire it given that you have a password. The dataset is described with citations in 5.2. Statistics missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors provide the values of the code parameters in the readme per experiment. The acutal values and architectures can be found in the code, although a central overview is missing. Values are also described in text in section 5. Acquisition not specified.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors perform 5 folds cross validation reporting average and standartd deviation over AUPRC, Mean Rank. For MIMIC they report on the dataset's test set.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
