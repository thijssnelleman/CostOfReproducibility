## Neur2RO: Neural Two-Stage Robust Optimization
Justin Dumouchelle, Esther Julien, Jannis Kurtz, Elias Khalil
Keywords: 
ICLR/2024/Proceedings/18583 - Neur2RO: Neural Two-Stage Robust Optimization.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the abstract (https://github.com/khalil-research/Neur2RO). In the readme they reference two papers that this codebase contains, high level overview of the repository, examples how to run the code, how and where to add new problems and models to the structure. There are no installation details. Code has good comments. Structure is large and needs a better index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors describe the problems Knapsack and Capital Budgetting in section 4 and appendix A including the parameters. Code and data on it available in implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

HP values per problem given in appendix I.2. table 12 and refer for the architecture to figure 3. They state in I.2. that no tuning was done, yet the values are not the same between problems, thus leaving the question how the values were acquired.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors detail the data split in sec 4. The authors measure Median RE, solving times (seconds) on the validation set (single model).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
