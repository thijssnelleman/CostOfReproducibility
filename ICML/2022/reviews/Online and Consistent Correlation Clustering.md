
## Online and Consistent Correlation Clustering
Vincent Cohen-Addad, Silvio Lattanzi, Andreas Maggiori, Nikos Parotsidis
Keywords: 
ICML/2022/Proceedings/17637 - Online and Consistent Correlation Clustering.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors state in 5.3 their code is written in C++ and provide a link to it (https://github.com/google-research/google-research/tree/master/online_correlation_clustering). In the readme they state how to compile the code, how to run the code, the parameters and how to set them, what the input should look like and how the output is formatted. The code has an acceptable amount of comments. The repository is small and easy to oversee. Pseudo code is given in algorithm 1&2. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

The authors state the datasets in section 5.1. In table 1 they summarise the datasets. A citation is provided and the data is very briefly described, more information welcome. A direct link is given in the citation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The algorithms pseudo code denote a parameter epsilon. The main parameters of the code take a beta and lambda value. These two are set in agree-off in sec 5.2. to 0.2. Its unclear whether agree-on also needs these parameter values.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors evaluate the method on 'relative correlation clustering', 'cumulative recourse', 'maximum recourse' (subfield specific metrics, requires an understanding of the concept of recourse) and cumulative running time. The results are single runs. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on graph clustering, specifically correlation clustering. 
