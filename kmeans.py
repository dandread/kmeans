# create a simple unsupervised machine learning program to perform
# naïve k-means clustering

import math
import statistics

f = open("kmeans.txt", "r")  # open kmeans.txt for reading points from file

# define variables stored in kmeans.txt
N = int(f.readline())  # max number of iterations
p = int(f.readline())  # number of points in input file
k = int(f.readline())  # total number of clusters

c = []  # index location of cluster centroids
# use 'for' loop to insert index location of cluster centroids into list
for line in range(3, 7):
    i = f.readline()
    c.append(int(i))  # strip whitespace

points = []  # x,y coordinates for each point
# use 'for' loop to insert point coordinates into list
for i in range(7, 107):
    coord = f.readline(i).split(',')  # delineate each line (coordinate) by comma
    x = int(coord[0])  # set first value of each line to x
    y = int(coord[1])  # set second value of each line to y
    points.append([x, y])  # create ordered pairs

# list of clusters; each inner list represents points within a cluster
# order corresponds to order in 'c'
# i.e. clusters[1] holds points closest to c[1] (centroid one)
clusters = [[], [], [], []]
prior_length = []
new_length = []

distances = []  # list containing distance from each centroid for all points

itr = 0  # number of iterations necessary to reach stability

for i in range(N):

    for j in range(p):
        distance = []  # list to hold distances of a point from each cluster
        for index in c:
            cluster = index
            # calculate distance of a point from each cluster
            d = math.sqrt((points[j][0] - points[cluster][0]) ** 2
                          + (points[j][1] - points[cluster][1]) ** 2)
            distance.append(d)
        distances.append(distance)
        distance = []

        # check to see which cluster point is closest to and append
        # point to closest cluster in list 'clusters'
        m = min(distances[j])
        if distances[j][0] == m:
            clusters[0].append(points[j])
        elif distances[j][1] == m:
            clusters[1].append(points[j])
        elif distances[j][2] == m:
            clusters[2].append(points[j])
        elif distances[j][3] == m:
            clusters[3].append(points[j])

    # calculate new length of clusters after re-clustering
    for z in range(3):
        new_length.append(len(clusters[z]))
    # check to see if cluster lengths have changed
    # once cluster lengths stop changing, stability is reached
    if new_length != prior_length:
        itr += 1
    prior_length = new_length
    new_length = []

    # calculate new centroid positions and update centroid locations in
    # 'points' by taking average of x and y values for each cluster
    x = [[], [], [], []]  # store all x values
    x_avg = []  # average x-values for each cluster
    y = [[], [], [], []]  # store all y values
    y_avg = []  # average y-values for each cluster
    new_centroids = []  # coordinates of new centroid
    for m in range(k):
        for j in range(len(clusters[m])):
            x[m].append(clusters[m][j][0])  # add all x-values by cluster
            y[m].append(clusters[m][j][1])  # add all y-values by cluster
        x_avg.append(statistics.mean(x[m]))  # average x-values by cluster
        y_avg.append(statistics.mean(y[m]))  # average y-values by cluster
        # create coordinates of new centroids
        new_centroids.append([x_avg[m], y_avg[m]])

    # update centroid coordinates in 'points'
    for index in c:
        cluster = index
        if cluster == c[0]:
            points[cluster] = new_centroids[0]
        elif cluster == c[1]:
            points[cluster] = new_centroids[1]
        elif cluster == c[2]:
            points[cluster] = new_centroids[2]
        elif cluster == c[3]:
            points[cluster] = new_centroids[3]

    # empty clusters, distances for re-clustering except on final iteration
    if i < N-1:
        clusters = [[], [], [], []]
        distances = []

# output results in specified format
# print number of iterations to achieve stability
print(f'Iterations to achieve stability: {itr}')
for index in c:
    cluster = index
    # print index of centroid in list 'c' - represents the centroid
    # in questions
    print(f'Centroid {c.index(cluster)}: {points[cluster]}')
    # print the number of points in each cluster
    print(f'Number of points in Cluster {c.index(cluster)}:'
          f' {len(clusters[c.index(cluster)])}')
    # print list of points in each cluster
    print(f'Cluster {c.index(cluster)}: {clusters[c.index(cluster)]}')
