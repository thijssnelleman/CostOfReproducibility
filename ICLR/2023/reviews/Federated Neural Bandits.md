## Federated Neural Bandits
Zhongxiang Dai, Yao Shu, Arun Verma, Flint Xiaofeng Fan, Bryan Kian Hsiang Low, Patrick Jaillet
Keywords: 
ICLR/2023/Proceedings/10831 - Federated Neural Bandits.pdf
Project URL: https://openreview.net/attachment?id=38m4h8HcNRL&name=supplementary_material

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their code in appendix E (https://github.com/daizhongxiang/Federated-Neural-Bandits). The readme states how to install, how to run their scripts and where the results can be found. The code is very unstructured and has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors conduct synthetic experiments on specified functions in 5.1 with descriptions, file seems to be present in the repo. They also use shuttle and magic telescope and provide a citation. Description on the later two is not present, links in the appendix.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

HP values in text in appendix E. No structured overview of acquisition given

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors report the mean and standard deviation across 3 runs. Results are across training curves. They measure cumulative regret.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[5]

-
