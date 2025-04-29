## SKDBERT: Compressing BERT via Stochastic Knowledge Distillation
Zixiang Ding, Guoqing Jiang, Shuai Zhang, Lin Guo, Wei Lin
Keywords: ML: Learning on the Edge & Model Compression, CV: Learning & Optimization for CV, CV: Representation Learning for Vision, SNLP: Language Models, SNLP: Learning & Optimization for SNLP, SNLP: Text Classification
AAAI/2023/Proceedings/25902 - SKDBERT: Compressing BERT via Stochastic Knowledge Distillation.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch? 

[5]

2. Implementation of specific method is missing: +3, but I feel the implementation of the method
   is actually not too complicated and they give code to another repository where the method was
   tested. Adding their method to this repository should be simple. However, since this leaves us
   with no code to observe how the method was evaluated and compared I still add 3 points and not
   less. 
2A. The method was used on top of the implementation here
    (https://github.com/huawei-noah/Pretrained-Language-Model/tree/master/TinyBERT) which gives a lot of details on the general implementation of the distillation but no implementation of the specific 
method or experiments. Therefore I would increase cost here by +1
2B. Figures are available but no pseudo-code: +1
2C. Nothing relevant observed


### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1) 

9/9 if counting the individual tasks of the dataset

1. There is a direct link to the dataset on page 7417, but citations are given in-depth
2. Datasets are described in the appendix
3. There are not statistics over the dataset +1
4. The dataset does not seem to be private

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

1. Hyperparameters are clearly stated in the Apendix in Table 5.
2. Hyperparameter values appear to be given in a good overview in Table 5 as well.
3. It is not given how the hyperparameters have been acquired and therefore also not what budget
   was used if any +2



### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

1. Metrics being used are given in Table 4 and are standard
2. Glue-dev has been used to evaluate the models which is a standard split available.
3. I can't really find information on the strategy to acquire the evaluations. I assume single run
   but can't even find if multiple seeds have been used. +2
4. Since no information about multiple seeds is given I can't really judge the aggregation of
   results and would assume they used a single seed. But only an assumption +1.


### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

I think you need some background and of course some code digging/reading about tinyBERT, but then
I have the feeling that using the tinyBERT repository and the available information in the paper
the work should be repeatable without major obstacles or super complex domain knowledge.