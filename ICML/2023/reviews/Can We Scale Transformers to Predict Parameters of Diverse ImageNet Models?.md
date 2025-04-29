
## Can We Scale Transformers to Predict Parameters of Diverse ImageNet Models?
Boris Knyazev, DOHA HWANG, Simon Lacoste-Julien
Keywords: 
ICML/2023/Proceedings/24569 - Can We Scale Transformers to Predict Parameters of Diverse ImageNet Models?.pdf
Project URL: nan

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation in the subtitle of the paper (https://github.com/SamsungSAILMontreal/ghn3). In the readme they introduce the method, post updates/news, provide installation instructions, point to a setup script for the data, provide an example how to use the code, and point to which script provides what experiment. The code is rich in comments. A tutorial notebook is also available in the examples.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use a public dataset which they cite and describe briefly. Download instructions are available in the implementation. More details on the data would be welcome.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[2]

The authors state they tune hyperparameters in accordance to a previous work but do not state any details. The authors state learning rate sensitivity in appendix A.3. They also conduct a neural architecture search in A.4. They list the hp values used in section 5. Its a bit unclear how exactly what was optiimised and it will take some effort to fully understand this.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors evaluate accuracy and test split is specifeid in section 5. The authors report average and std dev of the top 10 are reported out of the various architectures per method.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[4]

Requries expertise on transformers and transfer learning.
