## Hyperparameter Tuning with Renyi Differential Privacy
Nicolas Papernot, Thomas Steinke
Keywords: 
Award: Outstanding Paper Award
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[9]

The authors state they implement their method in JAX in section 3. No other details given.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[5]

(1/1)

The authors finetune a CNN on MNIST. No details on the dataset are provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors list various hyperparameter values in section 3. They use their method to finetune the learning rate, but fix all other values. Structured overview missing.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors report the mean training accuracy over 500 runs on the training set of MNIST.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
