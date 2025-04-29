
## PromptFix: You Prompt and We Fix the Photo
yongsheng yu, Ziyun Zeng, Hang Hua, Jianlong Fu, Jiebo Luo
Keywords: 
NeurIPS/2024/Proceedings/93588 - PromptFix: You Prompt and We Fix the Photo.pdf
Project URL: https://www.yongshengyu.com/PromptFix-Page/

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[4]

The authors provide a link to their porject page, where they link their implementation (https://github.com/yeates/PromptFix). In the readme they introduce the method, show examples, a table of contents, how to install, how to infer, where to download the data set with direct link and automatic downloader, high level statistics on the dataset, how to train and ackownledgements for other implementations used in theirs. The code has few comments. The stable diffusion directory has its own readme but its unclear what exactly waas implemented by the authors and what is taken elsewhere as no index is given. Overview is given in figure 2 and pseudo code in algorithm 1. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors describe the data set used in details in appendix A with a direct link and statistics. They also provide an overview on the data in figure 6. More details are given in the implementation docs.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors state hyperparmaeter values in 5.1. They state one value (delta) was set empirically (no budget). In appendix A.3. they state a few more details but none regarding the acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors state metrics used in 5.1. with citations but no explanations. The results are single model/run. The authors sample 200 test images to produce the results on and there are also some notes in this in section 3. Full details are not given on this data set split.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on NLP and CV, image generation/modification and diffusiuon models.
