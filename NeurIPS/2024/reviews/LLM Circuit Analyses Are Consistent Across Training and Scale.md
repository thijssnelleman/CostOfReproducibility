
## LLM Circuit Analyses Are Consistent Across Training and Scale
Curt Tigges, Michael Hanna, Qinan Yu, Stella Biderman
Keywords: 
NeurIPS/2024/Proceedings/96762 - LLM Circuit Analyses Are Consistent Across Training and Scale.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[3]

The authors state in the appendix regarding neurips checklists their code is included in the supplementary material. No link to it can be found however, when looking on the openreview / neurips publication page of the paper we do find the code (https://proceedings.neurips.cc/paper_files/paper/2024/file/47c7edadfee365b394b2a3bd416048da-Supplemental-Conference.zip). This is directly linked from the publication page of NeurIPS and is therefore considered documentation. A direct link to it in the paper would be preferred. In the readme they state installation instructions, an overview of the structure with details of some code files and where to find scripts to run for experiments and visualisation. Notebooks are also included. The code could use some more comments. The overview of the structure is nice but should be more detailed due to the sheer size of the directory.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(4/4)

Datasets are included in the zip file of the implementation. The authors state in section 2.4 the task and source for the IOI datasets (included in zip), for the gendered-pronoun they create it themselves (straight forward and included), greater-than is cited and explained and which generator is used (also included) and parameters given, subject-verb agreement is explained and cited but seemingly not included but a direct link is provided in the citations. Statistics given are very shallow however.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors conduct an analysis on previous methods. No training/finetuning done so not applicable.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The metrics per dataset are denoted in section 2. The metrics are details in appendix D. The results are single model. No data split applicable (analysis). 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

Requires expertise on LLMs and NLP tasks.
