def recommend_users(profile_manager, graph, user):
    user_interests = profile_manager.users[user]["interests"]
    scores = []

    for other in profile_manager.users:
        if other != user and other not in graph[user]:
            common = user_interests & profile_manager.users[other]["interests"]
            scores.append((other, len(common)))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores