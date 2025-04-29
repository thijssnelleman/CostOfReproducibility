
## 🏘️ ProcTHOR: Large-Scale Embodied AI Using Procedural Generation
Matt Deitke, Eli VanderBilt, Alvaro Herrasti, Luca Weihs, Kiana Ehsani, Jordi Salvador, Winson Han, Eric Kolve, Aniruddha Kembhavi, Roozbeh Mottaghi
Keywords: 
Award: Outstanding Paper
NeurIPS/2022/Proceedings/2856 - 🏘️ ProcTHOR: Large-Scale Embodied AI Using Procedural Generation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors discuss publishing the implementation on GitHub in the supplementary material but no link can be found.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[5]

(0/1)

The authors present a new dataset in section 4, provide detailed statistics on it and describe it. They source it by generation from their model. The pre-processing/ cleaning is explained in appendix B.8. The authors state the intent to make it public but no link can be found. The model used to generate the data is also not linked/public, complicating this process.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the hyperparameters of the experiments in appendix F, mainly table 4 but also in text with motivation. They state they were adapted from a previous work (Acquisition). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors provide a dataset split in appendix B.8.1. and section 4. Benchmark dataset is specified per results. Metrics are 'Success', SR and SPL (Citations provided in the appendix), but these are not defined. Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on procedural 3D generation.
