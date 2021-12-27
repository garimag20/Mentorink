import pandas as pd
import io
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def machine_learning(username, state, interest1, interest2, interest3, gender, career, language):
    df = pd.read_csv("C:/Users/Kalash Jain/Desktop/team-74/resources/ML/mentor_data.csv")
    # df.drop(['password', 'phonenumber','name', 'no_of_students'], axis = 1, inplace= True)
    
    df = df.append({"username" : str(username), "state" : state,"interest1" : interest1,"interest2" : interest2, "interest3": interest3, "gender": gender, "career" : career, "language" : language}, ignore_index=True)

    # print(df)
    
    df.set_index('username', inplace = True)

    # print(df)
    
    indices = pd.Series(df.index)
    print(indices[0:5])

    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            words = words + str(row[col])+ ' '
        row['bag_of_words'] = words

    # df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)
    
    count = CountVectorizer()
    count_matrix = count.fit_transform(df['bag_of_words'])
    
    
    # print(indices[0:5])
    
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    
    return recommendations(df, username, cosine_sim, indices)
    
    
def recommendations(df, username,  cosine_sim, indices):

    recommended_mentors = []

    idx = indices[indices == username].index[0]

    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)

    top_10_indexes = list(score_series.iloc[1:11].index)

    for i in top_10_indexes:
        recommended_mentors.append(list(df.index)[i])

    return recommended_mentors
    




