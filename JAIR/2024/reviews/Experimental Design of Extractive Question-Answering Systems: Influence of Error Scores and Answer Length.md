
## Experimental Design of Extractive Question-Answering Systems: Influence of Error Scores and Answer Length
Amer Farea, Frank Emmert-Streib
Keywords: 
JAIR/2024/Proceedings/15642 - Experimental Design of Extractive Question-Answering Systems: Influence of Error Scores and Answer Length.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors give an overview of the method in figure 1. No implementation given. The authors do reference a package and specify code file in 3.2.6. which could give a starting point.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use the SQuAD dataset, provide a citation and description and statistics in table 2. The authors also measure the frequency of anser lengths in number of words in the datasets in figure 3. No direct link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state the various training parameters they used for fine tuning distilbert in table 4 (grid evaluation). 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use exact match and f1 score as metrics and define them in 3.2.5. Results are single fine-tuning runs of distilbert on the SQuAD dataset. It is specified per experiment on which dataset and subset the result is presented, data split is specified in sec 3.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[7]

Requires expertise on NLP and LLMs.
