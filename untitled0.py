# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 16:38:54 2018

@author: D3XT3R
"""
 #Item based Collaborative Filtering is an algorithm based on the similarity between 
 #items so that they can provide suggestions to users.
 #Step 1: Read the data and create the input matrix 


import numpy as np
import math

# Read the data to numpy array
with open('user_data.csv', 'r') as input_data:
    raw_data = input_data.read()
    data = [row.split(',')[1:] for row in raw_data.split('\n')][1:]
    data = np.array(data, dtype=np.float)

print(raw_data)
print()
print(data)


#Step 2: Calculate similarities between movies
#The similarity here is calculated based on the cosine distance:
   # Suppose we calculate the similarities of the two films m1 and m2,we find that these two films are evaluated by the user u2 and u3 (as in the data above).
   # We will create 2 item-vector v1 for m1 and v2 for m2 in user-space (u2, u3).
   #v1 = 5 u2 + 3 u3 
   #v2 = 2 u2 + 3 u3
   
   # The cosine similarity is then calculated by the formula:
   #cos(v1, v2) = (53 + 23) / sqrt[(25 + 9) * (4 + 9)] = 0.9037
   
   # Similarly, repeating with each pair of different movies, we can calculate the similarities between them. The result will be the similarity matrix between the movies.
   
   
   
n_user,n_movie=data.shape
similarity_matrix=np.diag(np.ones(n_movie))

upper=lambda a:a[0]*a[1]
lower=lambda b:b[0]*b[0]+b[1]*b[1]

def cal_cosin_distance(similarity_vector):
    upper_sum=np.sum(np.apply_along_axis(upper,1,similarity_vector))
    lower_sum=math.sqrt(np.prod(np.apply_along_axis(lower,0,similarity_vector)))
    distance=upper_sum/lower_sum
    return distance

for m in range(n_movie):
    for n in range(m+1,n_movie,1):
        similarity_vector=data[np.where((data[:,m]!=-1)*(data[:,n]!=-1))][:,(m,n)]
        distance=cal_cosin_distance(similarity_vector)
        similarity_matrix[m,n]=distance
        similarity_matrix[n,m]=distance
        print("Movie 1:{} and Movie 1:{} have the similarity of:{}\n".format(m,n,distance))
print("Similarity matrix between movies:")
print(similarity_matrix)



def cal_rating(user_rating_vector, target_movie):
    upper = 0.
    lower = 0.
    for m in range(n_movie):
        if user_rating_vector[m] == -1 or m == target_movie: continue
        upper += user_rating_vector[m] * similarity_matrix[target_movie, m]
        lower += similarity_matrix[target_movie, m]
    rating = upper/lower
    return rating
    
unrated_movie = np.zeros((n_user, n_movie), dtype=np.float32)

# For each user and for each movie that user hadn't rated yet, predict rating for that user - movie pair
for u in range(n_user):
    for m in range(n_movie):
        if data[u, m] == -1:
            user_ratings = data[u, :]
            unrated_movie[u, m] = cal_rating(user_ratings, m)
print("Original data:")
print(data)
print()
print("Predict rating only data:")
print(unrated_movie)


# Find the max rating
recommend_movie = unrated_movie.argmax(axis=1)
for user, movie in enumerate(recommend_movie): 
    print("Recommend movie {} for user {}".format(movie, user))
