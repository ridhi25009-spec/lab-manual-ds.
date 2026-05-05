from collections import defaultdict

class SocialGraph:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_connection(self, u, v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def remove_connection(self, u, v):
        self.graph[u].discard(v)
        self.graph[v].discard(u)

    def get_friends(self, user):
        return list(self.graph[user])