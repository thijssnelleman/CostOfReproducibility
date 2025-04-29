## Unbiased Gradient Boosting Decision Tree with Unbiased Feature Importance
Zheyu Zhang, Tianping Zhang, Jian Li
Keywords: Machine Learning: ML: Applications, Machine Learning: ML: Classification
IJCAI/2023/Proceedings/0515 - Unbiased Gradient Boosting Decision Tree with Unbiased Feature Importance.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

github
implementation, an example script, a dozen files, experimental data as database files
+1 no comments in code

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(60/60)

name of the (well known) source, I know they are public from the fact that those sources are public ones. all ather details are in an appendix that's only available on the arxiv version of the paper (name of the dataset, some stats, and an algorithm showing how they were picked. No direct link nor description)

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

specify HPO tool, search space and number of epoch
Do not clearly state the found values +4
But they are likely in the db which they load in their example script. -1


### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

use standard measure, aggregate based on cited literature and explain it in a few words.
details about splits are a bit confusing +1
implied strategy +1


### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

some maths but with the code available you shouldn't really need to understand them to reproduce. 
