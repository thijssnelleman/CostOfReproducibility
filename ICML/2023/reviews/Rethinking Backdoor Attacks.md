
## Rethinking Backdoor Attacks
Alaa Khaddaj, Guillaume Leclerc, Aleksandar Makelov, Kristian Georgiev, Hadi Salman, Andrew Ilyas, Aleksander Madry
Keywords: 
ICML/2023/Proceedings/23636 - Rethinking Backdoor Attacks.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors state some documentation will be available in their code in footnote 12. No implementation shared. Overview on the concept are given in figure 1 and 2. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(1/1)

The authors use a public dataset and cite it. Direct link provided, no description or statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors list the HPs in table 5 of the appendix. On these models trained under the HPs they conduct attacks of various categories and variable values. Other than that this category is not really applicable (the authors do not present their own method with HPs rather they evaluate other methods).

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors measure various standard metrics such as ROC/AUROC but also use some task specific metrics such as poisened examples. This requires some expertise in adversarial attacks to understand. The authors measure accuracy of the models with/without the attacks in table 1. Each model is trained on 50% of the dataset at random. The authors state they train 100k models per experiment and setup. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on adversarial learning and backdoor attacks.
