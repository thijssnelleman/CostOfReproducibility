## Measuring the Objectness of Image Windows
Bogdan Alexe, Thomas Deselaers, Member, Vittorio Ferrari
Keywords: Objectness measure, object detection, object recognition
extra_reviews/2012/Proceedings/Measuring the Objectness of Image Windows.pdf


### Implementation
_Given the documentation shared by the authors on a new method, how much effort would it be to re-implement the method from scratch?_

[3]

The authors provide a link to their implementation in the introduction (https://people.ee.ethz.ch/~calvin). This link is currently dead. After some searching we determined the new link where the source code has moved to (https://calvin-vision.net/bigstuff/objectness/objectness-release-v2.2.zip) which is an updated version of the original code. The readme has instructions on installation and how to use with examples, code example explanations, descriptions on provided outputs (mainly the windows for the Pascal VOC dataset), and a changelog. The file structure is rather large and could use an index, especially because some of it seems to be not their own code. The code has some comments, but some code is quite cryptic. Implementation details in 2.6.

### Data
_Given the data description in the documentation, how much effort would it take to either: Find the same data set the authors used, or a similar data set and defend the comparability, or acquire one from scratch?_

[2]

(1/1)

The authors use PASCAL VOC 07 (cited), describe its usage in sec 3 and sec 5. Some statistics are provided in text. No direct link.

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for obtaining the reported results, and compare them against their computation budget?_

[4]

The authors describe parameters in section 2. A structured overview is missing. There are also some default params listed in the code. Acquisition not always specified. Overall it will take some effort to determine which settings were used per experiment.

### Experimental Procedure
_Given the setup of experiments reported in the work, how difficult is it to set up a new experiment with the same procedure, similar to those presented in the original work?_

[1]

The authors use the static t/v/t splits from the dataset (sec 3). The authors measure DR-#WIN (explained) over single runs.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying solely on the available documentation?_

[3]

-
