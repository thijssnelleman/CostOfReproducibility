
## MuChin: A Chinese Colloquial Description Benchmark for Evaluating Language Models in the Field of Music
Zihao Wang, Shuyu Li, Tao Zhang, Qi Wang, Pengfei Yu, Jinyang Luo, Yan Liu, Ming Xi, Kejun Zhang
Keywords: Application domains: Music and sound, Methods and resources: AI methods for better understanding human creative processes, Methods and resources: AI systems for collaboration and co-creation, Methods and resources: Computational implementations inspired by fields such as psychology or cognitive science, Methods and resources: Datasets, knowledge bases and ontologies, Theory and philosophy of arts and creativity in AI systems: Autonomous creative or artistic AI, Theory and philosophy of arts and creativity in AI systems: Cultural and social impacts of AI on creativity, creative practice, education and society, Theory and philosophy of arts and creativity in AI systems: Ethical issues raised by creative AI systems, Theory and philosophy of arts and creativity in AI systems: Evaluation and curation of artistic or creative artefacts, Theory and philosophy of arts and creativity in AI systems: Other theory or philosophy of arts and creativity in AI, Theory and philosophy of arts and creativity in AI systems: Social (multi-agent) creativity and human-computer co-creation
IJCAI/2024/Proceedings/0860 - MuChin: A Chinese Colloquial Description Benchmark for Evaluating Language Models in the Field of Music.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors present a new public benchmark data set and provide a link (https://github.com/CarlWangChina/MuChin/) where they provide evaluation/scoring code. The repository is well structured and documented with readmes. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The newly created dataset is publicly available, the authors present an overview of the data, some key statistics, and how the data set was constructed in section 3.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors evaluate pretrained models and cite their sources in 4.2. No training/configuration is done on their method.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate pretrained models on their new data set. They provide implementations of their metric calculations in the repository, and the formulas are detailed in the appendix which is placed in the repository. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires a good understanding of NLP to understand the data and tasks presented.
