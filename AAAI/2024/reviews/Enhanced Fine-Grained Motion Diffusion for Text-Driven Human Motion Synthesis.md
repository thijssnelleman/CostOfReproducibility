
## Enhanced Fine-Grained Motion Diffusion for Text-Driven Human Motion Synthesis
Dong Wei, Xiaoning Sun, Huaijiang Sun, Shengxiang Hu, Bin Li, Weiqing Li, Jianfeng Lu
Keywords: CV: Biometrics, Face, Gesture & Pose, CV: Language and Vision, CV: Vision for Robotics & Autonomous Driving, HAI: Applications
AAAI/2024/Proceedings/28784 - Enhanced Fine-Grained Motion Diffusion for Text-Driven Human Motion Synthesis.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do no provide any implementation source. However, the authors do provide a section regarding implementation details of the model (The frame work it was implemented with) but otherwise mainly contains hyperparameter values. There are a few diagrams and examples provided that can help. No pseudo code or framework designs given, which in this case makes is a lot of effort to re-implement.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors evaluate on 2 data sets, which they provide citations on and a small description. The authors describe all metrics briefly. The authors seem to indicate these are public data sets but this is not stated explicitly and no links to where they can be acquired are given, so this would have to be determined based on the citation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The authors give architecture settings and hyperparameter values for the model in the implementation details, but it is unclear if some could be missing. It is unclear how these were acquired. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The data set split procedure is discussed and cited. They provide details on how the metrics were collected in their table caption. It is unclear if the train/test split each time is also randomised or just the seed for training. This could perhaps be collected from one of their citations.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires expertise regarding motion diffusion models, especially on the practical side because no implementation source is given.
