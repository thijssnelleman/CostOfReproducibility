
## Scalable Primal Heuristics Using Graph Neural Networks for Combinatorial Optimization
Furkan Cantürk, Taha Varol, Reyhan Aydoğan, Okan Örsan Özener
Keywords: 
JAIR/2024/Proceedings/14972 - Scalable Primal Heuristics Using Graph Neural Networks for Combinatorial Optimization.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 1 (https://github.com/furkancanturk/gnn4co). In the readme they state where to download the files, how to isntall the requirements and how to run the code to reproduce the experiments. The code needs more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors use five CO datasets: MSC, CA, MIS and FCMNF, GIS. All have citations provided. A download link is given in the readme. Details are a bit lacking. The authors also generate instances for each problem, and describe the process in 5.1. and code is available. More details are given in appendix B. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state the hyperparameters in 5.2. and conduct a grid search for the delta parameter and specify the selected values but the grids are not given. A structured overview is missing.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state the evaluation metrics with formulas in 5.3. The results are presented as boxplots and averaged. Each cofnigruation discussed in sec 5 is presented seperatily. The population is not completely clear. Its not completely clear on which split the results are presented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on GNNs, combinatorial optimisation.
