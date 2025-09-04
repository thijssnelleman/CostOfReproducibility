## Explicit Box Detection Unifies End-to-End Multi-Person Pose Estimation
Jie Yang, Ailing Zeng, Shilong Liu, Feng Li, Ruimao Zhang, Lei Zhang
Keywords: 
ICLR/2023/Proceedings/12138 - Explicit Box Detection Unifies End-to-End Multi-Person Pose Estimation.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the abstract (https://github.com/IDEA-Research/ED-Pose). In the readme they give an overview on the method, results and model zoo per dataset with links to the models, installation instructions, where to download and how to prepare the data, and loads of examples how to run the code per dataset. The code has ok comments, but the structure is quite large and could use an index.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use CrowdPose and COCO, provide download links in the implementation but little other information.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors conduct an analysis on the hyperparameters in section 5.3. and summarise the used values in appendix A. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors evaluate the model on the test sets (given by the dataset) over single runs, measuring Loss, AP, AP50, AP75, APM, APL and Time [ms] (explained).

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
