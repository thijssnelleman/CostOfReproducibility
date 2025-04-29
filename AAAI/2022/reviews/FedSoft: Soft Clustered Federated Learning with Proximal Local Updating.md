
## FedSoft: Soft Clustered Federated Learning with Proximal Local Updating
Yichen Ruan, Carlee Joe-Wong
Keywords: Machine Learning (ML)
AAAI/2022/Proceedings/20785 - FedSoft: Soft Clustered Federated Learning with Proximal Local Updating.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[10]

The authors do not provide a source for their implementation, nor are any details of it shared. They provide a pseudo code of their method in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(3/3)

The authors use three data sets in their experiment, one of which is synthetic and they provide the details/formulas under which its generated. The other two data sets are popular benchmark data sets. The first they provide details and desciptions on with citations, the second is put in the technical report which is not included but can in this case be accepted as less impactfull on the effort as other details are already provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[3]

The authors provide full hyperparamter values on their method, however those of the client methods seem to be missing. The real impact of this requires subfield specific expertise to determine. The acquisition of their own parameter values is not specified.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The experiments section provides details on how many clients are used and how the data is distributed. They state the test is evaluated on  a holdout data set 'from their corresponding cluster distributions', but for local models they evaluate on the local training datasets. The authors state the metrics used, which are standard. It requires some expertise to fully understand the set up of this experiment.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

The method requires a deep understanding of federated learning to fully understand and reproduce the procedures presented.
