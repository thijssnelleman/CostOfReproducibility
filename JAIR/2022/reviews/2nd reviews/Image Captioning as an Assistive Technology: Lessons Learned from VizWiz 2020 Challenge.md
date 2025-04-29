## Image Captioning as an Assistive Technology: Lessons Learned from VizWiz 2020 Challenge
Pierre  Dognin, Igor Melnyk, Youssef Mroueh, Inkit Padhi, Mattia  Rigotti, Jarret  Ross, Yair  Schiff, Richard A. Young, Brian  Belgodere
Keywords: 
JAIR/2022/Proceedings/13113 - Image Captioning as an Assistive Technology: Lessons Learned from VizWiz 2020 Challenge.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

There is no link to an implementation given (+4).
The authors mention they used a ResNeXt model, but do not provide details on how it was implemented or where it was obtained from. The only implementation detail I could find mentions that their web-based demo uses python. (+4)  
There are multiple figures showing the author's pipeline and model architectures, and the caption of Figure 3 gives slightly more details, but no pseudocode is given (+1).  

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors used the VizWiz Captions dataset, which should be publically available from the VizWiz challenge website. A link to the competition website is provided in the demo Github which, while it does not provide code, does contain additional links in the README. The challenge website contains more details.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

The author's method consists of many individual models and parts, all of which may contain their own sets of hyperparameters.  
Section 3 and 4 describe these architectures and provide some relevant parameters in the text, but fail to give an overview (+2).  
Some training hyperparameters (epochs, learning rate) are mentioned in Section 5.2, but no method for how they were determined is given (+2).  

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use various evaluation methods and provide explanations for all of them (without mathematical formulations).  
The dataset itself is split into multiple train and test sets, and the authors always mention which set is used for a given result.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

In general, as the underlying problem comes from a competition, the task is rather easy to understand.  
The method described is an accumulation of many, multi-modal approaches, and grasping the concepts of all of them does require substantially more effort if one is not familiar with them. It does appear that most of these methods are widely-used in the field, based on the author's description, so a reader that is somewhat familiar with image captioning should have at least heard of some of these methods before.
