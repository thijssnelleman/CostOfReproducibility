
## Automatic Recognition of the General-Purpose Communicative Functions Defined by the ISO 24617-2 Standard for Dialog Act Annotation
Eugénio Ribeiro, Ricardo Ribeiro, David Martins de Matos
Keywords: 
JAIR/2022/Proceedings/13280 - Automatic Recognition of the General-Purpose Communicative Functions Defined by the ISO 24617-2 Standard for Dialog Act Annotation.pdf
Project URL: 

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[8]

The authors state implementation details in 5.5. and state they use Keras + TensorFlow as framework wit citations. Overview in figure 1, 2, 3. No implementation given.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors state in 5.1. they use the DialogBank dataset (cited, discussed in section 2), the LEGO-ISO dataset (cited) and Switchboard Dialog Act Corpus (cited) and are described in 5.1.1, 5.1.2 and 5.1.3 with statistics in table 2-4. No links.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[5]

There is a note on hyperparameters in section 3. They state some details regarding the hyperparameters in 5.5, structured overview missing, no acquisition, and unclear if all needed details are there.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate the methods with leave-one-out cross-validation, and present/define the metrics in 5.2.3. Results are averaged + std deviation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[5]

Requires expertise on ISO standard and NLP.
