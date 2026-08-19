def monitor_following_distance(distances: list[float], speeds: list[float]) -> tuple[int, float, int]:
    """
    Analyzes following distance compared to safe distance (speed * 0.5).
    
    Args:
        distances (list[float]): Distance to the lead car at each second.
        speeds (list[float]): Speed of our car at each second.
        
    Returns:
        tuple[int, float, int]: (tailgating_seconds, minimum_distance, tailgate_incidents)
            - tailgating_seconds: total seconds distance was < safe distance
            - minimum_distance: absolute closest distance to the lead car (return 0.0 if empty list)
            - tailgate_incidents: number of separate instances the car started tailgating
    """
    seconds = 0
    incidents = 0
    tailgate = False

    for i in range(len(distances)):
        if (speeds[i] * 0.5) > distances[i]:
            seconds = seconds + 1
            if tailgate == False:
                incidents = incidents + 1
                tailgate = True
        else:
            tailgate = False

    smallest = 100000.0
    for i in range(len(distances)):
        if distances[i] < smallest:
            smallest = distances[i]
    if smallest == 100000.0:
        smallest = 0.0

    return seconds, smallest, incidents
