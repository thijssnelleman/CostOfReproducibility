
## MusicMagus: Zero-Shot Text-to-Music Editing via Diffusion Models
Yixiao Zhang, Yukara Ikemiya, Gus Xia, Naoki Murata, Marco A. Martínez-Ramírez, Wei-Hsiang Liao, Yuki Mitsufuji, Simon Dixon
Keywords: Application domains: Music and sound, Methods and resources: Machine learning, deep learning, neural models, reinforcement learning
IJCAI/2024/Proceedings/0864 - MusicMagus: Zero-Shot Text-to-Music Editing via Diffusion Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors do not share their implementation, but do provide direct links to many methods used to implement theirs. However, practical details on their implementation are absent. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[7]

(0/1)

The authors synthesise data from a pretrained model but these synthesations are not shared. They also state a quality selection process, but the details are missing. This makes it costly to reproduce the method as it is hard to approach their data acquisition strategy and defend why it is comparable.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The method itself is seemingly hyperparameter free based on figure 3.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors state and explain the metrics used per task, with citations provided for most of them. The authors state what data was used for the test and how they subsample it for the subjective test. In 5.5 the subjective experiment is explained in detail. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires an understanding of music analysis and generation.
