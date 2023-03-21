# tweet-sentiment-and-vaccine-uptake
Predicts vaccine uptake from tweet sentiment


Abstract:
The COVID-19 vaccines have reduced the spread of infection worldwide, but resistance remains high. Understanding underlying sociodemographic disparities and public sentiment is paramount in reducing vaccine hesitancy and increasing vaccine uptake. This study implements location-tagged social media data, collected over a 1-year period, to improve county-level forecasts of vaccine uptakes in California. 

A database of 1.76 million county-specific vaccine-related tweets (Jan 2021-Dec 2021) was assembled. Tweets were labeled with a sentiment score between [-1,1] using the pre-trained language model BERTweet, with 1 indicating a positive vaccine sentiment and -1 indicating negative. Socioeconomic indices, including Social Vulnerability Index, were included per county. Three models – Multilayer Perceptron Neural Network (MPNN), Random Forest, Bayesian Additive Regression Tree (BART) – were trained using Weka.

My hypothesis is validated: Twitter sentiment data improves vaccine uptake prediction. The best model, Random Forest, accurately predicts 88.36% of vaccine uptake counts, which is improved from existing methods that don’t use social media data (22.64%). Urban, metropolitan counties also demonstrate 10.3% higher positive sentiment compared to rural counties.

Social media data provide real-time, accurate indicators of changing vaccine hesitancy. These findings suggest the potential of social media data mining to identify county-level anti-vaccine sentiment and ensure equitable, effective COVID vaccine distribution.

