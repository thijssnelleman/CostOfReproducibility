## Human Parity on CommonsenseQA: Augmenting Self-Attention with External Attention
Yichong Xu, Chenguang Zhu, Shuohang Wang, Siqi Sun, Hao Cheng, Xiaodong Liu, Jianfeng Gao, Pengcheng He, Michael Zeng, Xuedong Huang
Keywords: Knowledge Representation and Reasoning: Common-Sense Reasoning, Natural Language Processing: Question Answering, Knowledge Representation and Reasoning: Reasoning about Knowledge and Belief
IJCAI/2022/Proceedings/0383 - Human Parity on CommonsenseQA: Augmenting Self-Attention with External Attention.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

+4 because no implementation
+1 because they point to what they use, with a link to github for one of the things they use, papers for the other stuff.
I find it hard to assess because they use several things and don’t give as good information for each (one has a git link, one has a paper, one has the name of the pretrained model) So I guess it could fall in your +2 category?

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]
2*0.25+6*0.75 = 5

(1/18)

There is one main dataset with citation and description. it's the one results are shown on. Score 2 because no direct link

there are 17 others with name, no link or description, some stats. They are used to train a key element of the method. They say it's in appendix but I didn't find the appendix : score 6

The weight for the 17 is larger because they are important to reimplement the method. The weight for the evaluation is lower because without it I could still reimplement the method though I would need to test it on something else.


### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

clearly stated, in text, with relation to original papers on which it's based
seeds not stated so maybe an other +1 ?

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[5]

using accuracy of best out of 3 runs, no information on the 2 others
no clear split (but the dataset has one so probably just use the one from dataset)

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[8]

Using many existing works, to reproduce and understand minimally what you're doing, you'd probably have to read at least 5 other papers (the model they use, the knowledge graph generation technique, etc...)