# Next Hike

## A Content based trail recommender

Hiking is a good way to exercise and spend time with friends and family, while also enjoying the surrounding nature. Many hikers rely on various trail websites to gain information about wide array of trails and decide on which new trails to hike on. While some of these websites provide trail recommendations they are largely based on geographic location of the hike they are currently viewing. For users who wish to find trails farther away, it is still up to the users to user search function to look through various trails and make decision on which one to take on next. 

The goal of this project is to:
- Build a trail recommender that takes user’s favorite trail as an input and recommend top 5 trails that are similar to the user input
- Deploy the recommender on Webapp for teseting

The recommendated trails are limited to be within the same state as user input, as trails too far away (i.e East Coast) would be less relevant as it would not be very practical. Here, we have used trails from CA for recommender, and the framework can be easily adopted and extended to other states.

## The data
### Data source
- The data was scraped from Alltrails.com using AWS, Selenium and beautiful soup
- Total of 1000 trails in CA and ~500000 reviews were collected
- Features for each trail consisted of trail stats (i.e. distance, elevation, difficulty, star rating) as well as descriptive texts (i.e tags, short and long descriptions)

## Modeling and Evaluation

### Baseline Model
First, a baseline model is established by making random recommendations. 

### Content based recommendation
  Similarity matrix between trails were calculated. Then, based on the user input, 5 trails with highest similarity was recommended to the user. Three different content based models were established:
  1. Trail stats similarity : Features such as distance, elevation, difficulty were used to calculate similarity. Gives recommendations based on trails stats.
  2. Text based similarity: Used NLP to obtain TF-IDF matrix, which was then converted to trail-trail similarity. Gives recommendations based on description of the trails (i.e scenary, accessibility, activities, trail conditions, etc) 
  3. Hybrid similarity: Combination of stats and text based similarity. Gives recommendations based on both trail stats and description. 

### Collaboratie filtering based recommendation 
  Collaborative filtering based recommendation models were built that utilizes ratings given by users. By using the user ratings, more personnalized recommendations can be given. Two different collaborative filtering models were built to predict star rating for user-item pair, generate recommendation based on top 5 predicted ratings per user:
  1. Item-item based collaobratie filtering: As there were more number of users than number of trails, item-item based filtering (as opposed to user-user based)
  2. Matrix factorization: SVP was used to reduce dimensionality 
  
  
### Evaluation metrics
  The most idealistic way to test recommender models would be to deploy the model and test the user response through A/B testing. As conducting such test is not possible, the existing data (or part of data) can be used to assess and compare performance. 
  
  
  
### Web deployment:



## Future directions:
In order to improve the prediction accuracy, we could:  
- Use the incorrectly predicted images to further train our model  
- Add more images (through web scraping or data augmentation)  
- Increase the model complexity to better capture the non-linear decision boundary

Additionally, I'd like to:
- Use transfer learning and compare prediction accuracy
- Add additional cuisines and test performance



