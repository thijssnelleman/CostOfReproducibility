
## DANets: Deep Abstract Networks for Tabular Data Classification and Regression
Jintai Chen, Kuanlun Liao, Yao Wan, Danny Z. Chen, Jian Wu
Keywords: Data Mining & Knowledge Management (DMKM)
AAAI/2022/Proceedings/20309 - DANets: Deep Abstract Networks for Tabular Data Classification and Regression.pdf

### Implementation

_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present their implementation online (https://github.com/WhatAShot/DANet). Settings, training and inference parameters are given. It is clear from the repository how to start with the code. 
Little comments are provided for the code. 
  

### Data

_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(6/7)

They use 7 datasets and 1 hyperoptimization tool. 
For one dataset, a link is provided but the url is broken (+2), for three datasets there is only a citation (+1 )
1 +2 because there is a kaggle link, but the url is broken 
2 +1  only citation
3 +1 only citation
4 +1 only citation
5
6
7
Descriptive statistics for each dataset. Each dataset +1 because there is no description beyond "regression" and "open-soure tabular"

### Configuration

_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

There is an explanation of the hyperparameters in the text +1, Training budget is not specified. 
  
### Experimental Procedure

_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

From context it seems accuracy and MSE are used for evaluation, this is explicitly stated  in the text. It is clear that performances are evaluated on the test set. It is unclear whether results are aggregated and over how many +2 . It is unclear therefore how results are aggregated +1 . There is some measure of distribution, but unclear what type +1. 

### Expertise

_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Most of the code is available on the github, they also provide code for creating the datasplits the way they did. The main issue would be finding all the data and training all the different networks. Also not knowing how the accuracy or MSE aggregation is done, or what random seed was used could lead to issues. You would have to read about all the different techniques you are comparing against and whether they reference them correctly. 
