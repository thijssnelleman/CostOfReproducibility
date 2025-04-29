
## Long-Short Term Cross-Transformer in Compressed Domain for Few-Shot Video Classification
Wenyang Luo, Yufan Liu, Bing Li, Weiming Hu, Yanan Miao, Yangxi Li
Keywords: Computer Vision: Recognition (object detection, categorization), Computer Vision: Video analysis and understanding, Machine Learning: Few-shot learning
IJCAI/2022/Proceedings/0174 - Long-Short Term Cross-Transformer in Compressed Domain for Few-Shot Video Classification.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors stated various other works used in their implementation paragraph but no practical details are shared (such as languages or libraries). No implementation shared. An overall framework is presented in figure 2 with a detailed presentation in figure 3. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(4/4)

The authors state they use four datasets, which are seemingly public, in their experiments, provide citations on them but no details are given on the datasets. No direct links provided. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors state various hyperparameter values in the implementation paragraph, but without (pseudo)code it is hard to verify if all required values are presented. No acquisition strategy is specified. The authors do a modular ablation study on their method in table 2.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The authors state the train/validation/test splits with their data set definition which are provided by the data definitions and state they report the results over 10k randomly sampled episodes from testing sets. The authors use accuracy as a metric. The results are single model/run, based on the results / data definitions.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on transformers, LSTM and few shot classification which are alot of different domains the independent investigator would need to have varying levels of expertise on.