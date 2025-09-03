## Scaling Laws for Neural Machine Translation
Behrooz Ghorbani, Orhan Firat, Markus Freitag, Ankur Bapna, Maxim Krikun, Xavier Garcia, Ciprian Chelba, Colin Cherry
Keywords: 
ICLR/2022/Proceedings/6721 - Scaling Laws for Neural Machine Translation.pdf
Project URL: nan

### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[10]

The authors do not provide an implementation.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[9]

(1/2)

The authors use an in-house web-crawled training dataset and specify the languages and how many sentence pairs. For evaluation they use WMT2019 evaluation campaign (cited). There is almost no information on the inhouse dataset yet this is crucial as it is used for training. The evaluation dataset is briefly noted.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[6]

Hyperparameters are not tuned and they use a previous work for the values. Some values are stated in appendix C. It is not clear if all values are reported.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors evaluate BLEU, test loss, and cross entropy loss on back-translated data. Data splits clear. Results are single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[7]

-
