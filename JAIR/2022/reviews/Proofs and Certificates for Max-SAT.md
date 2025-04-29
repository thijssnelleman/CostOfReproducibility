
## Proofs and Certificates for Max-SAT
Matthieu Py, Mohamed Sami Cherif, Djamal Habet
Keywords: 
JAIR/2022/Proceedings/13811 - Proofs and Certificates for Max-SAT.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors provide a link in footnote 2 for the source code (https://pageperso.lis-lab.fr/matthieu.py/en/software.html) but this link does not work. Pseudo code available. The authors state they implemented it in C++. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors evaluated the method on the benchmark instances of the 2020 Max-SAT evaluation, for which they provide a project page link where download links can be found. The authors state the number of instances but otherwise provide little information on them.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method is parameter free.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use a time out of 1 hour and 16 GB of memory. The authors measure time in seconds over the instances and percentage of proved instances over % of empty clause proved as well as proof size in bytes over the instances. The type of resolutions are summarised in absolute numbers and percentages in table 2.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise on Max-SAT.
