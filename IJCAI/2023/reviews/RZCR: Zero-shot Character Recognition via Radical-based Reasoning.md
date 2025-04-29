
## RZCR: Zero-shot Character Recognition via Radical-based Reasoning
Xiaolei Diao, Daqian Shi, Hao Tang, Qiang Shen, Yanzeng Li, Lei Wu, Hao Xu
Keywords: Computer Vision: CV: Vision and language, Multidisciplinary Topics and Applications: MDA: Humanities
IJCAI/2023/Proceedings/0073 - RZCR: Zero-shot Character Recognition via Radical-based Reasoning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors present the overall architecture in figure 3, general overview of the task in figure 1 and 2 and pseudo code in algorithm 1. The implementation is not shared, nor are any details on it.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(3/4)

The authors introduce a new dataset in this work, and state from which data sets they source it in 5.1 but the dataset itself is not published. These sources have citations and statistics/descriptions. There is also a link to some data provided in 4.2. Furthermore they state they evaluate their method also on three other methods which are seemingly public. Not a lot of information is given on the seemingly public datasets.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state a few fixed architecture design / hyperparameter values in 5.1 for all experiments. It is difficult to verify if all needed values are presented for reproduction as a search space / hyperparameter space of the method is not presented. There is no explanation on how these values were acquired.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[6]

The authors state they present top-n prediction by confidence to present the average classification accuracy. The authors state they validate on the non-private data set but it is unclear how it was validated on their own data set (OracleRC) as no split is stated. The training procedure will also take some effort to extract.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires experience with OCR/CV methods, and zero-shot learning.
