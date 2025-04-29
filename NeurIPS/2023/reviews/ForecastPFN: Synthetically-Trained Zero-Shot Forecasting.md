
## ForecastPFN: Synthetically-Trained Zero-Shot Forecasting
Samuel Dooley, Gurnoor Singh Khurana, Chirag Mohapatra, Siddartha V Naidu, Colin White
Keywords: 
NeurIPS/2023/Proceedings/70200 - ForecastPFN: Synthetically-Trained Zero-Shot Forecasting.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation (https://github.com/abacusai/forecastpfn). In the readme they state how to install, how to run inference with a trained model, hiw ti geberate synthetic data and how to train a model. The parameters/configurations are described. Code has good comments. Structure is overseeable but barely.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(8/8)

The authors seven benchmark datasets which they detail in appendix E.3. They provide citations on each and a brief description. Minor statitstics are given. More information would be welcome. A data generator can also be found in the code that is described in sec 3.1. in detail. No direct links found.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors discuss hyperparameter values in appendix E.2. and E.3. but a structured overview or acquisition is not clear.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

Metrics are MSE over wins. The authors aggregate results over the datasets in figure 4 with standard deviation. The authors train on the synthetic data and use it for all evaluations. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on zero-shot methods and time-series data.
