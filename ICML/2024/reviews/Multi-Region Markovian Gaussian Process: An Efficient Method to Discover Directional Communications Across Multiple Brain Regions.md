
## Multi-Region Markovian Gaussian Process: An Efficient Method to Discover Directional Communications Across Multiple Brain Regions
Weihan Li, Chengrui Li, Yule Wang, Anqi Wu
Keywords: 
ICML/2024/Proceedings/32806 - Multi-Region Markovian Gaussian Process: An Efficient Method to Discover Directional Communications Across Multiple Brain Regions.pdf
Project URL: https://github.com/WeihanLikk/MRM-GP

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide their implementation online (https://github.com/WeihanLikk/MRM-GP). In the readme the authors provide a link to their paper, installation instructions and where to find step by step tutorials for the code. The tutorials have very few text blocks/comments. The code could also use some more comments in general. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

The authors use three datasets for the evaluation of their method. Two dataset files are available in the GitHub. There are descriptions given on each dataset with citations. No statistics provided. The generation code is either not present or not clearly documented in the implementation. The generation and its parameters / distributions are specified in 5.1. The generated data is not present in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the hyperparameters in both tutorials in the implementation. The hyperparameters of the method are summarised in section 4. These values are also stated in 5.2. and 5.3. The authors state one of the paramaters is dependent on the data, and another is determined through 'cross validation strategy' (grid search). The budget for this is specified. For the other parameters, the values are only given. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state the experimental setup per data set. They state how the datasets are split into training and testing. The metrics are all time related and they state the metrics used in section 5. The experiment is averaged 'over five distinct partitions'.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires experience with markovian gaussian proccesses and the tasks presented. 
