## Deep convolutional and LSTM recurrent neural networks for multimodal wearable activity recognition
Francisco Javier Ordóñez, Daniel Roggen
Keywords: human activity recognition, wearable sensors, deep learning, machine learning, sensor fusion, LSTM, neural network
extra_reviews/2016/Proceedings/Deep convolutional and LSTM recurrent neural networks for multimodal wearable activity recognition.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in the conclusion through a citation, which has been moved but is automatically resolved (https://github.com/STRCWearlab/DeepConvLSTM). In the readme they state a description on the work, and link the paper as well as how to run the model with a notebook. The notebook is an extensive example that automatically downloads a dataset and preprocesses it. There are alot of comments and descriptions. The same holds true for the other code files. There are no installation instructions.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors provide automatic downloading in the repository for the Opportunity UCI dataset. They also use Skoda dataset. Both are cited, have lengthy descriptions and tables with task details or statistics (fig 4, table 2). Link for Skoda dataset is in the citation.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[2]

The authors define the hyperparameters and architecture variables in the example notebook in the code in a seperate block with descriptions of each. There is a discussion on the values in 5.3 although acquisition is a bit lacking for some (only layers are evaluated).

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[3]

The authors measure F1 score (eq. 11) and static data splits are clarified in 4.1.1 for OPPORTUNITY, but for Skoda this is not clear. Results are single run. It is also not always clarified in each caption whether the result is on train or test, which will need to be validated with some effort.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
