
## SAlign: A Graph Neural Attention Framework for Aligning Structurally Heterogeneous Networks
Shruti Saxena, Joydeep Chandra
Keywords: 
JAIR/2023/Proceedings/14427 - SAlign: A Graph Neural Attention Framework for Aligning Structurally Heterogeneous Networks.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors state a link to their implementation in the abstract (https://github.com/shruti400/SAlign). The repository only contains some data files and two pdfs with results. The authors state they use PyTorch as a framework.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three datasets: Douban Online-Offline, Allmovie-IMDB and DBLP. Each is described and cited. statistics in table 2. One data set seems to be available in the implementation, but in general links are not provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors state they tune the HPs using grid search algorithm from Hyperopt. The values are discussed in section 5. No structured overview. No details on what the grids were and which HPs were considered for tuning. No budget.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors state the metrics insection 5 with explanation and citations. All results are averaged over 30 trials. The data split is not completely clear from section 5 or on what they present the results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on GNN and attention mechanisms.
