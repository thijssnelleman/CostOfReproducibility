## Auto-Transfer: Learning to Route Transferable Representations
Keerthiram Murugesan, Vijay Sadashivaiah, Ronny Luss, Karthikeyan Shanmugam, Pin-Yu Chen, Amit Dhurandhar
Keywords: 
ICLR/2022/Proceedings/6166 - Auto-Transfer: Learning to Route Transferable Representations.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors provide a link to their implementation in footnote 1 of the abstract (https://github.com/IBM/auto-transfer) but the repository is empty. An overview schematic is provided in figure 1 and pseudo code in algorithm 1-3. No other details.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(6/6)

The authors use ImageNet, CUB200, Stanford Dogs datasets, MIT67 and Stanford40 as datasets. The authors state they are benchmark datasets but provide no other details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors specify a few HP values in text in A.3. It is not clear whether this is complete. No structured overview or acquisition given.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[4]

The authors repeat each experiment (runs) three times and present accuracy but the aggregation/variation is not explained. The authors seem to use a random proportion split for training/testing although it is not very clearly specified.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[6]

-
