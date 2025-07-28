
## “Allot?” is “A Lot!” Towards Developing More Generalized Speech Recognition System for Accessible Communication
Grisha Bandodkar, Shyam Agarwal, Athul Krishna Sughosh, Sahilbir Singh, Taeyeong Choi
Keywords: Deep Learning, Machine Learning, Automatic Speech Recognition, Audio And Speech Processing, Wav2vec 2.0, Sound, Computation And Language, Data Augmentation, Accented Speech
AAAI/2024/Proceedings/32445 - “Allot?” is “A Lot!” Towards Developing More Generalized Speech Recognition System for Accessible Communication.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors state they use a model/method called Wav2Vec but do not provide an implementation of this. Although this implementation could be straight forward (using Wave2Vec docs), it would still be welcome for this purpose, especially regarding the data transformation applied (Noise injections for their experiments).

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(3/3)

The authors use three public data sets and cite the source, provide statistic on them

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors show in two tables which hyperparmeters will be optimised and motivate it is only a subset of all available hyperparameters. They motivate their hyperparameter choices based on limitations of computational resources, indicating a human search optimised towards resource usage (instead of the usual objective function).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors clearly state the metrics used in their evaluation. They show the augmentations done for each experiment and indicate a one shot representation of the results. A more detailed explanation exactly how the runs were conducted would be welcome, but it can be made out from context.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[1]

The method is quite comprehensive and detailed in their instructions. Relatively little pre-knowledge required.
