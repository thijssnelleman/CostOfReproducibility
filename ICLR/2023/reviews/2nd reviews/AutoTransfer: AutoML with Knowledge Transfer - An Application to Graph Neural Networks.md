## AutoTransfer: AutoML with Knowledge Transfer - An Application to Graph Neural Networks
Kaidi Cao, Jiaxuan You, Jiaju Liu, Jure Leskovec
Keywords: 
ICLR/2023/Proceedings/11462 - AutoTransfer: AutoML with Knowledge Transfer - An Application to Graph Neural Networks.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide their implementation online (https://github.com/snap-stanford/AutoTransfer). The repo contains info on how to run training examples and how to download the dataset. The code is very poorly commented and the structure of the repo is not easy to navigate. Total cost increases by 2.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(6/6)

The authors release a large-scale dataset with reproducible configuration and training performance on a range of tasks (with a link to it). They benchmark their method on 6 public datasets. The datasets come with citations, without a direct link or statistics (+2).

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[3]

The hyperparameter space for GNN is stated in the Appendix, with an overview table. Final hyperparameter values are not explicitly provided, but the best performing configurations were saved in the repo for reproducibility purposes (unless I am very mistaken... here you can do +1 if needed). I am unsure how exactly the hyperparameters were tuned (I saw mentions of TPE and random search, but I currently lack clarity... so this also can be increased). In general, my gut feeling tells me that, even though the information might be there, it requires very careful checking of the paper and the repo in parallel to find everything. Therefore my total score would be around 3-4 here.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The main evaluation metric is very common (accuracy), and other auxiliary metrics are properly introduced, defined and cited (Kendall rank correlation). The train/test split of the data is very clearly specified. Strategy is clear, 30 independent runs. The results are averages and std is reported. I don't see a huge problem with this part.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

The repo is quite confusing, I believe that it would require decent effort to nail down all details even though some parts might seem straighforward.