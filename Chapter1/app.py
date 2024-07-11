"""Module providing a function printing dictionary prettier"""

from collections import defaultdict, Counter
from pprint import pprint

users = [
    {"id": key, "name": value}
    for key, value in enumerate(
        [
            "Hero",
            "Dunn",
            "Sue",
            "Chi",
            "Thor",
            "Clive",
            "Hicks",
            "Devin",
            "Kate",
            "Klein",
        ]
    )
]
# print(users)

friendship_pairs = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

# Initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# And loop over the friendship pairs to populate it
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

pprint(friendships)


def number_of_friends(user):
    """How many friends does _user_ have?"""
    source_user_id = user["id"]
    friend_ids = friendships[source_user_id]
    return len(friend_ids)


total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)
num_users = len(users)
# average connections per user
avg_connections = total_connections / num_users

print(avg_connections)

# find the most connected people
# create a list of user id and number of friends
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)
pprint("num_friends_by_id")
pprint(num_friends_by_id)


def friend_of_a_friend(user):
    """Find a friend of the given user"""
    source_user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[source_user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != source_user_id and foaf_id not in friendships[source_user_id]
    )


print(friend_of_a_friend(users[3]))

interests = [
    (0, "Hadoop"),
    (0, "Big Data"),
    (0, "HBase"),
    (0, "Java"),
    (0, "Spark"),
    (0, "Storm"),
    (0, "Cassandra"),
    (1, "NoSQL"),
    (1, "MongoDB"),
    (1, "Cassandra"),
    (1, "HBase"),
    (1, "Postgres"),
    (2, "Python"),
    (2, "scikit-learn"),
    (2, "scipy"),
    (2, "numpy"),
    (2, "statsmodels"),
    (2, "pandas"),
    (3, "R"),
    (3, "Python"),
    (3, "Statistics"),
    (3, "regression"),
    (3, "probability"),
    (4, "machine learning"),
    (4, "regression"),
    (4, "decision trees"),
    (4, "libsvm"),
    (5, "Python"),
    (5, "R"),
    (5, "Java"),
    (5, "C++"),
    (5, "Haskell"),
    (5, "programming languages"),
    (6, "statistics"),
    (6, "probability"),
    (6, "mathematics"),
    (6, "theory"),
    (7, "machine learning"),
    (7, "scikit-learn"),
    (7, "mahout"),
    (7, "neural networks"),
    (8, "neural networks"),
    (8, "deep learning"),
    (8, "Big Data"),
    (8, "artificial intelligence"),
    (9, "Hadoop"),
    (9, "Java"),
    (9, "MapReduce"),
    (9, "Big Data"),
]


def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest"""
    return [
        user_id
        for user_id, user_interest in interests
        if user_interest == target_interest
    ]


print(data_scientists_who_like("HBase"))

interests_by_user_id = defaultdict(list)
user_ids_by_interest = defaultdict(list)
for user_id, user_interest in interests:
    interests_by_user_id[user_id].append(user_interest)
    user_ids_by_interest[user_interest].append(user_id)

pprint(interests_by_user_id)
pprint(user_ids_by_interest)


def most_common_interests_with(user):
    """Find the users of common interests with the given user"""
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )


print(most_common_interests_with(users[3]))

# salaries and tenures
salaries_and_tenures = [
    (83000, 8.7),
    (88000, 8.1),
    (48000, 0.7),
    (76000, 6),
    (69000, 6.5),
    (76000, 7.5),
    (60000, 2.5),
    (83000, 10),
    (48000, 1.9),
    (63000, 4.2),
]

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

avarage_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

pprint(avarage_salary_by_tenure)


def tenure_bucket(user_tenure):
    """Set up buckets based on the tenure"""
    if user_tenure < 2:
        return "less than two"
    if user_tenure < 5:
        return "between two and five"
    return "more than five"


# keys are tenure buckets and values are list of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    BUCKET = tenure_bucket(tenure)
    salary_by_tenure_bucket[BUCKET].append(salary)

# keys are tenure buckets, values are average salary for that bucket
average_salary_by_tenure_bucket = {
    bucket: sum(salaries) / len(salaries)
    for bucket, salaries in salary_by_tenure_bucket.items()
}

pprint(average_salary_by_tenure_bucket)


experience_and_account_status = [
    (0.7, "paid"),
    (1.9, "unpaid"),
    (2.5, "paid"),
    (4.2, "unpaid"),
    (6.0, "unpaid"),
    (6.5, "unpaid"),
    (7.5, "unpaid"),
    (8.1, "unpaid"),
    (8.7, "paid"),
    (10.0, "paid"),
]

experience_by_status = defaultdict(list)
for experience, status in experience_and_account_status:
    experience_by_status[status].append(experience)

avg_experience_by_status = {
    status: max(experience) for status, experience in experience_by_status.items()
}

pprint(avg_experience_by_status)


# def predict_paid_or_unpaid(years_of_experience):
#     pass


words_and_counts = Counter(
    word for user_id, interest in interests for word in interest.lower().split()
)

pprint(words_and_counts)

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
