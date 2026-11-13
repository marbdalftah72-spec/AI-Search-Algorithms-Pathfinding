import heapq
from typing import Dict, List, Tuple, Optional

def a_star_search(graph: Dict[str, List[Tuple[str, float]]], 
                  heuristics: Dict[str, float], 
                  start: str, 
                  goal: str) -> Tuple[Optional[List[str]], float, int]:
    """
    A* Search Algorithm returning (path, total_cost, nodes_expanded).
    f(n) = g(n) + h(n)
    """
    frontier = []
    heapq.heappush(frontier, (heuristics.get(start, 0.0), 0.0, start, [start]))
    visited_cost = {start: 0.0}
    expanded_count = 0

    while frontier:
        f_val, g_val, current, path = heapq.heappop(frontier)
        expanded_count += 1

        if current == goal:
            return path, g_val, expanded_count

        for neighbor, edge_cost in graph.get(current, []):
            new_g = g_val + edge_cost
            if neighbor not in visited_cost or new_g < visited_cost[neighbor]:
                visited_cost[neighbor] = new_g
                new_f = new_g + heuristics.get(neighbor, 0.0)
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf'), expanded_count
