
## Landmark Heuristics for Lifted Classical Planning
Julia Wichlacz, Daniel Höller, Jörg Hoffmann
Keywords: Planning and Scheduling: Search in Planning and Scheduling, Planning and Scheduling: Planning Algorithms
IJCAI/2022/Proceedings/0647 - Landmark Heuristics for Lifted Classical Planning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation (https://github.com/minecraft-saar/powerlifted). They state in the paper they based their approach on a previous work with citation, and the original implementation can be easily found through the link. The readme has extensive documentation on how to run the code with various parameter options/explanations, a list of requirements, links to other used work, limitations and references to used papers. The code base is pretty huge and does not have an index. The code could also use more comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(8/8)

The authors briefly state they use a benchmark set with citation. They use eight benchmark datasets by the looks of table 1. Some statistics could also be determined from table 1. No other details are provided. The data sets can be found in the implementation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors discuss eight configurations (which seem to be modular) and evaluate each in table 1. These planning/heuristic functions are discussed in length in section 2 and 3. The implementation docs have a full description of the available options/parameters for the method. Based on the usage instructions, some of these values are missing in the definition in the paper so there will be some 'reverse engineering' needed to determine all the values. The parameters are evaluated on a grid.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure runtime and 'coverage', a task/problem specific metric used in the subfield. The results are single runs over the full datasets. The maximum time limit was set to 30 mins for all runs. It will take some experience in the subfield to understand the exact measurements, but in general the procedure is well documented.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires expertise in AI planning to understand the problem and method/heuristics/data sets presented.
