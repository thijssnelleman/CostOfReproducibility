
## Path Counting for Grid-Based Navigation
Rhys Goldstein, Kean Walmsley, Jacobo Bibliowicz, Alexander Tessier, Simon Breslav, Azam Khan
Keywords: 
JAIR/2022/Proceedings/13544 - Path Counting for Grid-Based Navigation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors link the library used as base and cite/link it and state they extended it with their implementation but do not provide this extension. Development in C++. Pseudo code in alg 1/2.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use Baldur's Gate II, Dragon Age: Origins and StarCraft from Sturtevant (cited, no link). The problems are described and statistics are provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

Methods are (based on alg 1 and 2) parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors measure average path lengths and average runtime/number of expansions per search over all the problems per benchmark dataset. The authors also explain the 10-40% results in 3.3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on path finding.
