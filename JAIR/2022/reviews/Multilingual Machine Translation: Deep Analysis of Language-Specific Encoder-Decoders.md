
## Multilingual Machine Translation: Deep Analysis of Language-Specific Encoder-Decoders
Carlos Escolano, Marta R. Costa-jussà, José A. R. Fonollosa
Keywords: 
JAIR/2022/Proceedings/12699 - Multilingual Machine Translation: Deep Analysis of Language-Specific Encoder-Decoders.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors link a tool they use for visualisation. They also st state the experiments were done with model implementations from Fairseq and provide a link and version number in footnote 4. Overview in figure 1 and pseudo code in algorithm 1. Implementation not given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[3]

(3/3)

In 4.1 the authors state they use EuroParl (citation), Yandex (link) and newstest2012/2013 (link). No other details than a few high level statistics.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

Hyperparameters are stated informally in 4.1. Overview/acuiqisition not given.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors use BLEU as metric. The data sets have their role regarding training/testing assigned in 4.1. Results are single model.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requires expertise on NLP.
