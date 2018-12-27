# Recommender System
# Introduction
 Recommendation system (sometimes replacing "system" with a synonym such as platform or engine) is a subclass of information filtering system that seeks to predict the "rating" or "preference" a user would give to an item.
 Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general. 
# Libraries

# Steps
 Item based Collaborative Filtering is an algorithm based on the similarity between 
 items so that they can provide suggestions to users.
 ### Step 1: Read the data and create the input matrix 
 
 ### Step 2: Calculate similarities between movies
   The similarity here is calculated based on the cosine distance:
   Suppose we calculate the similarities of the two films m1 and m2,we find that these two films are evaluated by the user u2 and u3 (as      in the data above).
   ### We will create 2 item-vector v1 for m1 and v2 for m2 in user-space (u2, u3).
   `v1 = 5 u2 + 3 u3 
    v2 = 2 u2 + 3 u3
   `
   ### The cosine similarity is then calculated by the formula:
   `cos(v1, v2) = (53 + 23) / sqrt[(25 + 9) * (4 + 9)] = 0.9037`
   
   ### Similarly, repeating with each pair of different movies, we can calculate the similarities between them. The result will be the      similarity matrix between the movies.
   
   ### Step 4: Find the predicted movie with the highest rating
   At the last step, we sort the results in the predicted matrix and select the highest rated result to suggest to the user.
