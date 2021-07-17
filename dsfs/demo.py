users = [ 
    { "id" : 0 , "name" : "Hero" }, 
    { "id" : 1 , "name" : "Dunn" }, 
    { "id" : 2 , "name" : "Sue" }, 
    { "id" : 3 , "name" : "Chi" }, 
    { "id" : 4 , "name" : "Thor" }, 
    { "id" : 5 , "name" : "Clive" }, 
    { "id" : 6 , "name" : "Hicks" }, 
    { "id" : 7 , "name" : "Devin" }, 
    { "id" : 8 , "name" : "Kate" }, 
    { "id" : 9 , "name" : "Klein" }
]

friendship_pairs = [( 0 , 1 ), ( 0 , 2 ), ( 1 , 2 ), ( 1 , 3 ), ( 2 , 3 ), ( 3 , 4 ), ( 4 , 5 ), ( 5 , 6 ), ( 5 , 7 ), ( 6 , 8 ), ( 7 , 8 ), ( 8 , 9 )] 

# dictionary comprehension
friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

# How many friends does user have?
def num_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

# generator comprehension?
total_connections = sum(num_of_friends(user) for user in users)

num_users = len(users)

avg_connections = total_connections / num_users

num_friends_by_id = [(user["id"], num_of_friends(user)) for user in users]

num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True
)

# friend of a friend finder
def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]
    ]

def foaf_ids_real(user):
    user_id = user["id"]
    
    init = [foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id] and foaf_id]

    fin = []
    for i in init:
        if i not in fin:
            fin.append(i)

    return fin

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
    )


interests = [ ( 0 , "Hadoop" ), ( 0 , "Big Data" ), ( 0 , "HBase" ), 
( 0 , "Java" ), ( 0 , "Spark" ), ( 0 , "Storm" ), ( 0 , "Cassandra" ), 
( 1 , "NoSQL" ), ( 1 , "MongoDB" ), ( 1 , "Cassandra" ), ( 1 , "HBase" ), 
( 1 , "Postgres" ), ( 2 , "Python" ), ( 2 , "scikit-learn" ), ( 2 , "scipy" ), 
( 2 , "numpy" ), ( 2 , "statsmodels" ), ( 2 , "pandas" ), ( 3 , "R" ), ( 3 , "Python" ), 
( 3 , "statistics" ), ( 3 , "regression" ), ( 3 , "probability" ), 
( 4 , "machine learning" ), ( 4 , "regression" ), ( 4 , "decision trees" ), 
( 4 , "libsvm" ), ( 5 , "Python" ), ( 5 , "R" ), ( 5 , "Java" ), ( 5 , "C++" ), 
( 5 , "Haskell" ), ( 5 , "programming languages" ), ( 6 , "statistics" ), 
( 6 , "probability" ), ( 6 , "mathematics" ), ( 6 , "theory" ), 
( 7 , "machine learning" ), ( 7 , "scikit-learn" ), ( 7 , "Mahout" ), 
( 7 , "neural networks" ), ( 8 , "neural networks" ), ( 8 , "deep learning" ), 
( 8 , "Big Data" ), ( 8 , "artificial intelligence" ), ( 9 , "Hadoop" ), 
( 9 , "Java" ), ( 9 , "MapReduce" ), ( 9 , "Big Data" ) ] 

# Inefficient because it searches entire list every call
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]

# Create dict mapping interest to users for efficient look up
from collections import defaultdict

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# Create dict mapping users to interests
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

# Returns users that given user has most common interests with
def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )

salaries_and_tenures = [( 83000 , 8.7 ), ( 88000 , 8.1 ), ( 48000 , 0.7 ), ( 76000 , 6 ), ( 69000 , 6.5 ), 
( 76000 , 7.5 ), ( 60000 , 2.5 ), ( 83000 , 10 ), ( 48000 , 1.9 ), ( 63000 , 4.2 )] 

# Keys are years, values are lists of the salaries fo each tenure.
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Look at the average salary for each tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}
# ^^^ This isn't very useful because none of the users have the same tenure

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

# Then we can group together the salaries corresponding to each bucket.
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# And finally compute the average salary for each group:
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

words_and_counts = Counter(word
                            for user, interest in interests
                            for word in interest.lower().split())


for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)








