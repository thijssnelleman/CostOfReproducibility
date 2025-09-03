## Multi-Task Processes
Donggyun Kim, Seongwoong Cho, Wonkwang Lee, Seunghoon Hong
Keywords: 
ICLR/2022/Proceedings/6487 - Multi-Task Processes.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to the implementation in the abstract (https://github.com/GitGyun/multi_task_neural_processes). In the readme they state how to run the code with example paramter values, and a requirements.txt file is available for installation. The code has ok comments but there is no indexing of the code, making is somewhat complicated to fully understand. Overviews given in fig 1 and 2.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use both synthetic and real world tasks, the first synthetic task is given in 5.1 and code is provided in the implementation. In 5.2 the authors use weather data, provide a description and a link + dataset file in the implementation, in 5.3 they use face data for which they describe how they construct the dataset and provide citations, further explaining in appendix F.1. that its CelebA HQ dataset but the link is missing.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors summarise architecture values in appendix B.4., table 5 and 6, training values are given in B.5. with values in table 7. Full config files are available in the implementation per experiment. Acquisition not specified for all values.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors state how the datasets are split in the appendix for training and testing. The authors measure average MSE and 1-mIoU, over 5 random seeds.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
