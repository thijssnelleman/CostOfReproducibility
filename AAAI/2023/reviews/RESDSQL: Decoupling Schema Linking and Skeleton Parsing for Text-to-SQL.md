
## RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL
Haoyang Li, Jing Zhang, Cuiping Li, Hong Chen
Keywords: SNLP: Lexical & Frame Semantics, Semantic Parsing, SNLP: Language Models
AAAI/2023/Proceedings/26535 - RESDSQL: Decoupling Schema Linking and Skeleton Parsing for Text-to-SQL.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a link to their implementation (https://github.com/RUCKBReasoning/RESDSQL). The implementation has an extensive readme with illustrations, updates, overview, results from the paper, requirements for usage and how to install them, directory structure needed and how to fetch their code, where to download the data and where to place them, step wise explanation on how to run the code for both training and inference. The code could definetily use more comments. The environments under which they ran their code is stated in the paper. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The data set used is linked in the implementation documentation, and they are described with meta info in the paper. Citations are provided.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state the values of the hyperparameters in the implementation details. However it is not clear how these values were acquired. This means independent investagors will have to defend possible differences regarding comparability.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The evaluation metrics are extensively discussed and sources are cited. Train/test splits on the data are provided. Single model/runs are presented as results.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[2]

The authors provide many examples on the problem, but their method is rather complex and will take some effort to understand. However with the presented implementation there are loads of examples to help you along the way.
