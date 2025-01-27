def calculateDistance(route, distance):
    totalDistance = 0
    for i in range (len(route) -1):
        totalDistance += distance[route[i]][route[i+1]]
    totalDistance += distance[route[-1]][route[0]]
    return totalDistance

def generatePermutation(elements):
    if len(elements) == 1:
        return [elements]
    permutation = []
    for i in range(len(elements)):
        rest = elements[:i] + elements[i+1:]
        for perm in generatePermutation(rest):
            permutation.append([elements[i]] + perm)
    return permutation


def travelingSalesManBruteForce(distances):
    cities = list(range(len(distances)))
    allRoutes = generatePermutation(cities)
    minDistance = float('inf')
    bestRoute = None
    for route in allRoutes:
        currentDistance = calculateDistance(route, distances)
        if currentDistance < minDistance:
            minDistance = currentDistance
            bestRoute = route
    return bestRoute, minDistance


if __name__ == "__main__":
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_route, min_distance = travelingSalesManBruteForce(distances)
    print(f"Best route: {best_route}")
    print(f"Minimum distance: {min_distance}")




