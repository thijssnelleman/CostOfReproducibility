
## Black Box Variational Inference with a Deterministic Objective: Faster, More Accurate, and Even More Black Box
Ryan Giordano, Martin Ingram, Tamara Broderick
Keywords: 
JMLR/2024/Proceedings/231015 - Black Box Variational Inference with a Deterministic Objective: Faster, More Accurate, and Even More Black Box.pdf
Project URL: https://github.com/rgiordan/DADVIPaper

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation as a link on the JMLR website (https://github.com/rgiordan/DADVIPaper) as well as on the first page of the paper where they state a second link for more general use as well (the given one is specifically regarding the results of the paper). In the readme they state how to install and how to run tests. They also link a repository regarding the experiments. Here they provide scripts with descriptions for reproduction. The code needs an index and more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(5/5)

The authors include data in their experiments repository. The datasets are described in 6.1 with citations. They summarise them as models in table 1. Statistics are provided on a high level, but more detailed statistics are needed to defend comparability to others. A link for tennis data is provided in fetch_tennis_data.sh.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors describe their method in algorithm 2. They fix N to 30 by default and examine the variance of this value in 6.5. There are no other input parameters defined. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Results for their method are over N = 30 draws. The metrics are runtime on a log10 scale and stochastic relative error (defined in 6.3.). Aggregation (when applicable) is mean. No variation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on black blox inference.
