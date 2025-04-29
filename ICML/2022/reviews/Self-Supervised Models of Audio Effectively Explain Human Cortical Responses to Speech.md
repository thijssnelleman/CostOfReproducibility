
## Self-Supervised Models of Audio Effectively Explain Human Cortical Responses to Speech
Aditya Vaidya, Shailee Jain, Alexander Huth
Keywords: 
ICML/2022/Proceedings/18093 - Self-Supervised Models of Audio Effectively Explain Human Cortical Responses to Speech.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[7]

The authors provide a link to an implementation (https://github.com/alexhuth/sensimetrics_filter) regarding 'stimulus preperation and presentation', but it does not seem their main implementation. In the readme there is a brief description on the code and the functions seem well documented. A real implementation is missing, but this does serve as a good starting point. Figure 1 gives an overview. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors collect their own data set which they publish publicly (https://openneuro.org/datasets/ds003020/versions/1.0.2). Extensive details regarding the acquisition are given in appendix D and section 2.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[9]

The authors use various medel architectures on their data sets, which they summarise in table 1.  A full overview on the HPs is missing. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors run each experiment with three different seeds, and for each run divded the data randomly 80-10-10 into tvt. It is not clear how the data was aggregated. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[3]

Requires expertise in the bio-medical domain and speech/audio/NLP data.
