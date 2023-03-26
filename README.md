# tweet-sentiment-and-vaccine-uptake
Predicts vaccine uptake from tweet sentiment


Abstract:
The COVID-19 vaccines have reduced cases worldwide, but resistance remains high. Currently, public health surveys are used to assess hesitancy ahead of roll-out to inform vaccine distribution. However, the lag-time and nonspecificity of surveys results in overestimated, inaccurate US vaccination predictions, leading to chaotic vaccine distribution and inefficient supply chains in highly vulnerable counties.

This study includes Twitter public sentiment to predict vaccine uptake in California counties through an optimized machine learning regression model. A database of 1.76 million
coordinate-tagged, COVID-vaccine-related tweets (Jan 2021-Dec 2021) was assembled and 1K
tweets sampled. Tweets were labeled with county-level socioeconomic indices (Digital Divide
Index, Social Vulnerability Index, Democratic Score) and a sentiment score using BERTweet.
Positive Twitter sentiment correlates with decreased vaccine hesitancies (r=0.575), and increased per-capita vaccine doses (r=0.429). Geographic region informs 59% of the variance between per-capita vaccine uptake rates (f=1.2) of urban and rural counties, suggesting geospatial disparities exist. Weka, a Java-based machine learning software, was used to construct three models: Random Forest, Bayesian Additive Regression Tree, and Multilayer Perceptron Neural Network. The best model, Random Forest, explains 91.4% (RMSE=0.1) of variability in vaccinated counts among CA counties, outcompeting existing models. This model provides health authorities and policymakers with a low-cost, high-accuracy monitoring system to predict county-level COVID-19 vaccine uptake. 

These findings further suggest the power of social media data mining in improving vaccine campaigns and optimizing vaccine roll-out.
