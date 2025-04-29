
## Robust Feature Rectification of Pretrained Vision Models for Object Recognition
Shengchao Zhou, Gaofeng Meng, Zhaoxiang Zhang, Richard Yi Da Xu, Shiming Xiang
Keywords: CV: Object Detection & Categorization, CV: Applications
AAAI/2023/Proceedings/25492 - Robust Feature Rectification of Pretrained Vision Models for Object Recognition.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

No source for their implementation is given. The authors provide implementation details regarding the Python/PyTorch versions used and some smaller details. They provide an architecture overview with few details in figure 3, and some examples. This means it will be quite the effort the re-implement the method as only the circumstances under which the code was run (language/library version) are given. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(4/4)

The authors describe 4 data sets they used for evaluation. No citations or statistics on the data sets are given. We recognise most of the named datasets as publicly available, however the lack of details means there will be more effort for independent investigators.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors introduce one hyperparameter regarding rectification loss in their work. Hyperparameter values are stated in the implentation details section. It is unclear whether these are all the values from the hyperparmaeter space needed, as there is no full description them nor is the implementation given to clarify. No details on how these values were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The auhtors measure accuracy over degradation levels and adress single degradation and composite. They state the backbones and training procedures on the data sets. The results are single models as stated.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

The method is presented on robustness in object recognition, and the authors measure distortion on various levels. They use various backbones and three widely used benchmark data sets to run their method on. The absence of the implementation can make it slightly more difficult to understand, but in general there are good examples and schematics presented and the concept its well introduced. 
