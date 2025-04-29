
## Probabilistic Forecasting with Generative Networks via Scoring Rule Minimization
Lorenzo Pacchiardi, Rilwan A. Adewoyin, Peter Dueben, Ritabrata Dutta
Keywords: 
JMLR/2024/Proceedings/230038 - Probabilistic Forecasting with Generative Networks via Scoring Rule Minimization.pdf
Project URL: https://github.com/LoryPack/GenerativeNetworksScoringRulesProbabilisticForecasting

### Implementation
_Given the documentation given by the authors on the method, how much time investment would it be to re-implement the method from scratch?_

[1]

The authors provide a link to their implementation on the JMLR website (https://github.com/LoryPack/GenerativeNetworksScoringRulesProbabilisticForecasting). In the readme they state which experiments code is provided, where to download datasets, additional result files, what each script does, how to install. Code has good comments.

### Data
_Given the data description in the documentation, how much effort take to either: Find the same dataset the authors used, or similar datasets and defend the comparability, or acquire one from scratch?_

[1]

(2/2)

The authors conduct simulation experiment in section 5.1. They state the models for simulation in appendix E with parameters and code is provided. 5.2. uses WeatherBench and they provide descriptions and statistics and a download link in the implementation. 

### Configuration 
_Given the (hyper)parameters, including semantic parameters, of the method: How much effort would it take to acquire the algorithm configurations used for their results, and compare against their budgetary constraints?_

[1]

The authors state they conduct hyperparameter tuning and the general setup in section 5 and that they report the final performance on the test sets. The hyperparameter optimal values are stated in table 4 for Lorenz63. The training HPs values and tested ranges are stated in E.2.3. For Lorenz96 the same is stated in E.3.3. For WeatherBench this is found in E.4.4. Optimisation is done on grid search.

### Experimental Procedure
_Given the experimental set-up of the work, how difficult is it to set up a new experiment, similar to those presented in the original work, with the same procedure?_

[1]

The authors provide the data splits per data set experiment, results are on the test set. The authors use Calibration Error, NRMSE, and R^2 as metrics (defined in section 5). Agregation is median and variation is 99% credible area over 10 forecasts.

### Expertise
_How much effort would it take to acquire the expertise required to reproduce the work independently relying on the available documentation?_

[6]

Requries expertise on probalistic forecasting and generative networks.
