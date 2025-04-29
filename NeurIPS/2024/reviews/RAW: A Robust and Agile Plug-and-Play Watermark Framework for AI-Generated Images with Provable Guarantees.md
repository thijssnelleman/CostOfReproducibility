
## RAW: A Robust and Agile Plug-and-Play Watermark Framework for AI-Generated Images with Provable Guarantees
Xun Xian, Ganghua Wang, Xuan Bi, Jayanth Srinivasa, Ashish Kundu, Mingyi Hong, Jie Ding
Keywords: 
NeurIPS/2024/Proceedings/93609 - RAW: A Robust and Agile Plug-and-Play Watermark Framework for AI-Generated Images with Provable Guarantees.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors do not share their implementation. A used library is cited and directly linked in the references. No practical details given in C.1.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[4]

(2/2)

The authors use two datasets namely MS-COCO and DBdifussion and provide citations on the in sec 4.1. with brief descriptions and minor statistics. No direct links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors evaluate two hyperparameters in sec 4.4. They set these values for the main results to 0.05. It does indicate how the authors selected the hyperparameter, but is not actually stated as the method for acquisition.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[3]

The evaluation metrics are described in 4.1. with citations although some could use more explanation. Each results is averaged over 5 independent runs and the std devs are stated at the end at 4.1. There is no specification of the train/test set. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requries expertise on generated images and watermark tasks and practical too since there is no implementation.
