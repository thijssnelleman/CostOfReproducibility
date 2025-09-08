## Dynamic Update-to-Data Ratio: Minimizing World Model Overfitting
Nicolai Dorka, Tim Welschehold, Wolfram Burgard
Keywords: 
ICLR/2023/Proceedings/11616 - Dynamic Update-to-Data Ratio: Minimizing World Model Overfitting.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation in footnote 1 of section 3 (https://github.com/Nicolinho/dutd). Readme has installation instructions, example on how to train the model with parameter values. Code has few comments.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[3]

(2/2)

The authors use Atari100k and DeepMind Control Suite and provide citations for both and are included in the code. Explanation are short.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[1]

The authors state they employ extensive gridsearch for their experiments HPs, which is done in 4.3. The authors provide a large config file with settings per dataset. 

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors run the experiments with 5/26 different seeds and provide 95% CI mean and median. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[4]

-
