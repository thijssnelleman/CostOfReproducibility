
## HeadSculpt: Crafting 3D Head Avatars with Text
Xiao Han, Yukang Cao, Kai Han, Xiatian Zhu, Jiankang Deng, Yi-Zhe Song, Tao Xiang, Kwan-Yee K. Wong
Keywords: 
NeurIPS/2023/Proceedings/73029 - HeadSculpt: Crafting 3D Head Avatars with Text.pdf
Project URL: https://brandonhan.uk/HeadSculpt/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state their code is coming soon on the repository link provided in the project page (https://github.com/BrandonHanx/HeadSculpt).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[8]

(0/2)

The authors discuss multiple datasets in section 3. A large 2D face dataset is used to train on, for which the authors provide several citations and technical descriptions how they transform it for 3D tasks, but it seems to be implied the data set is not public. Secondly, a tiny dataset D is mentioned for optimisation with some details, but this one also does not seem to be public. In general, there are a lot of open questions regarding data in this paper.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

Hyperparameters are defined in table 2. Acquisition not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[4]

The authors do a user study in figure 7 and describe the data collection in sec 4.2, but more details are welcome to ensure correctness of the study. In table 1 they calculate the CLIP metrics for 30 text prompts, but most details are refered to in a previous work.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on 3D CV and generation.
