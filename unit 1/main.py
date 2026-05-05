from profiles import ProfileManager
from graph import SocialGraph
from traversal import bfs_shortest_path, dfs_depth
from recommendation import recommend_users


def main():
    pm = ProfileManager()
    sg = SocialGraph()

    # Add users
    pm.add_user(1, "Ridhi", ["music", "coding", "travel"])
    pm.add_user(2, "Aman", ["coding", "sports"])
    pm.add_user(3, "Neha", ["music", "art"])
    pm.add_user(4, "Karan", ["sports", "travel"])
    pm.add_user(5, "Simran", ["art", "coding"])
    pm.add_user(6, "Raj", ["music", "sports"])

    # Update
    pm.update_profile(1, interests=["music", "coding", "fitness"])
    pm.update_profile(2, name="Aman Verma")

    # Show profiles
    print(pm.get_profile(1))
    print(pm.get_profile(2))
    print(pm.get_profile(3))

    # Connections
    sg.add_connection(1, 2)
    sg.add_connection(1, 3)
    sg.add_connection(2, 4)
    sg.add_connection(3, 5)
    sg.add_connection(4, 5)
    sg.add_connection(5, 6)
    sg.add_connection(2, 6)
    sg.add_connection(3, 6)

    sg.remove_connection(2, 6)

    # BFS
    print(bfs_shortest_path(sg.graph, 1, 5))
    print(bfs_shortest_path(sg.graph, 2, 3))

    # DFS
    print(dfs_depth(sg.graph, 1, 2))
    print(dfs_depth(sg.graph, 1, 3))

    # Recommendations
    print(recommend_users(pm, sg.graph, 1))


if __name__ == "__main__":
    main()