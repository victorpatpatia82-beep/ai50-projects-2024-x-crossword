def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    # If the source and target are the same, the path is empty
    if source == target:
        return []

    # Initialize the starting node
    start_node = Node(state=source, parent=None, action=None)

    # Use a QueueFrontier for Breadth-First Search (guarantees shortest path)
    frontier = QueueFrontier()
    frontier.add(start_node)

    # Initialize an empty set to keep track of explored people
    explored = set()

    # Keep searching until the frontier is empty
    while True:
        # If nothing is left in the frontier, the actors are not connected
        if frontier.empty():
            return None

        # Choose a node from the frontier
        node = frontier.remove()

        # Mark the current node as explored
        explored.add(node.state)

        # Add neighbors to the frontier
        for movie_id, person_id in neighbors_for_person(node.state):
            # Check if the person is neither in the frontier nor explored
            if not frontier.contains_state(person_id) and person_id not in explored:
                
                # Create the child node
                child = Node(state=person_id, parent=node, action=movie_id)

                # Early goal test: check if this neighbor is the target
                if child.state == target:
                    # We found the target! Reconstruct the path.
                    path = []
                    curr = child
                    # Loop backwards through the parents until we hit the source
                    while curr.parent is not None:
                        path.append((curr.action, curr.state))
                        curr = curr.parent
                    
                    # The path was built from target to source, so reverse it
                    path.reverse()
                    return path

                # If it's not the target, add it to the frontier to explore later
                frontier.add(child)
