
## Sign Language-to-Text Dictionary with Lightweight Transformer Models
Jérôme Fink, Pierre Poitier, Maxime André, Loup Meurice, Benoît Frénay, Anthony Cleve, Bruno Dumas, Laurence Meurant
Keywords: AI for Good: Multidisciplinary Topics and Applications, AI for Good: Computer Vision, AI for Good: Humans and AI, AI for Good: Natural Language Processing
IJCAI/2023/Proceedings/0662 - Sign Language-to-Text Dictionary with Lightweight Transformer Models.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[9]

The authors provide implementation details regarding the deployment but not of the training experiments. Implementations are not shared. Figure 1 shows a high level schematic of their implementation (both training and deployment). Figure 3 shows their architecture in a high level. 

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use a public data set, and discuss it in great length in section 4. They provide many statistics on the data and cite the sources. They also discuss how the data is used for their method. No direct link is available.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[4]

The authors analyse the effectiveness of 16 parameter configurations in table 2. However not all hyperparameters are considered, rather these are architecture parameters. Other hyperparameters are found in 5.2 with their values. Some values are explained with citations, others are simply stated. 

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors discuss the training procedure in 5.2, where they state the train/test split assumingly at random. They do state a few specifics for the split. They report training/testing accuracy, which is a straightforward metric. 

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requires some experience with the task (Sign language to text), transformers and computer vision.
