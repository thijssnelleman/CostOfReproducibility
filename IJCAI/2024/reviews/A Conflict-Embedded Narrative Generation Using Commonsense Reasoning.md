
## A Conflict-Embedded Narrative Generation Using Commonsense Reasoning
Youngrok Song, Gunhee Cho, HyunJu Kim, Youngjune Kim, Byung-Chull Bae, Yun-Gyung Cheong
Keywords: Application domains: Text, literature and creative language, Theory and philosophy of arts and creativity in AI systems: Autonomous creative or artistic AI, Theory and philosophy of arts and creativity in AI systems: Computational paradigms, architectures and models for creativity
IJCAI/2024/Proceedings/0857 - A Conflict-Embedded Narrative Generation Using Commonsense Reasoning.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[6]

The authors provide illustrations of their process in figure 2 and 3, and provide direct links to the sources they used to build their pipeline. However the implementation of the pipeline itself is missing, requiring still some effort to reimplement based on the documentation.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(2/3)

The authors provide a direct link + citations to their finetuning data set and the pretrained model they apply it to. For the candidate generation model the authors provide citations with short descriptions and a direct link to the pretrained model. It will still take some effort to acquire these, but basic information is given and data for comparison defence can be extracted from citations. The authors evaluated the method with a human experiment, but they do not publish the raw data.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[10]

No details regarding parameters / configurations.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The training procedure is stated with data sets and pretrained model, however a lot of details will have to be reverse engineered or extracted with quite some effort as the descriptions are rather short. The authors state the metrics used and how each is calculated. The authors state they apply a human evaluation and provide details on how this was conducted and evaluated.  

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires an understanding of NLP and the task to understand the framework/pipeline presented and needs practical experience with it in order to reproduce the method due to the lack of implementation documentation.
