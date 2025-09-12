
## The Complexity of Subelection Isomorphism Problems
Piotr Faliszewski, Krzysztof Sornat, Stanisław Szufa
Keywords: 
JAIR/2024/Proceedings/15550 - The Complexity of Subelection Isomorphism Problems.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[5]

The authors provide their implementation in footnote 3 (https://github.com/Project-PRAGMA/Subelections). There they provide two zipfiles, one for fig 1/2 and one for fig 3. In the readme they state installation instructions and how to run the code to repeat the experiments. The installation instructions are not enough based on the code. Requries more comments. Code requires an index. The code seems incomplete.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(18/18)

The authors use statistical models to generate elections in 5.1 and describe them. Parameter values are given. The authors provide a single file regarding this in the implementation but code seems to be missing. In 5.3. the authors use real life election data and provide citations and files are in the implementation. Descriptions are given and statistics are in table 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

N/A

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure time in seconds needed to find the maximum common voter subelections, with standard deviation over 1000 pairs of elections. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on election isomorphism problem.
