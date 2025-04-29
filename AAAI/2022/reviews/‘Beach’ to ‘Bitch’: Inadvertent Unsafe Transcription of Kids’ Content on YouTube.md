
## ‘Beach’ to ‘Bitch’: Inadvertent Unsafe Transcription of Kids’ Content on YouTube
Krithika Ramesh, Ashiqur R. KhudaBukhsh, Sumeet Kumar
Keywords: AI For Social Impact (AISI Track Papers Only)
AAAI/2022/Proceedings/21470 - ‘Beach’ to ‘Bitch’: Inadvertent Unsafe Transcription of Kids’ Content on YouTube.pdf

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[2]

The authors provide a project page (https://github.com/sumeetkr/UnsafeTranscriptionofKidsContent). Here the authors provide a brief readme, some notebooks to reproduce the papers results, and two data sets. In general its quite straightforward to run the notebooks, however as the notebooks are designed for a combination of code and neatly formatted text, its a shame the authors don't use this functionality more. It would also be a good idea to post details on the data set in the readme, for accessibility.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(1/1)

The authors create their own data sets, and publish them on their implementation repository. They provide many statistics on their datasets and extensive descriptions. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors use pretrained models and do not re-train them.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[2]

The authors take pretrained models and analyse their output as distance to the ground truth. They use one standard measure of distance in text, the phonetic distance is explained but could do with a more detailed explanation.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[1]

The method requires an entry level understanding of text based data science / ML.
