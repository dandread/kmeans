Summary
In this module, an unsupervised machine learning algorithm, k-means
clustering, was employed to create four groups of data points, each
group containing data points closest to a given centroid in that
group.

Setup
The text file kmeans.txt was provided and contains the information
necessary for the calculations performed in this program. To setup
the program, each line of the file was read into either a variable
or list as follows:

    1. The first line contains the maximum number of iterations the
       program should run.

    2. The second line contains the number of points in the input
       file, kmeans.txt.

    3. The third line contains the total number of desired clusters
       the program should group points in.

    4. Lines 3-6 contain the index location of the centroids in the
       list of points. These index locations were read into a list
       using a 'for' loop.

    5. The remaining lines of the program contain the x,y coordinates
       of all the points. Two issues arise here due to the fact that
       the coordinates are read into the list as strings, and not the
       expected integer type. First, accessing the x,y values for each
       point is impossible, and second, performing calculation on the
       points is impossible. The 'split()' operation was used to 'split'
       each line into two parts, using the ',' as a delimiter. Once the
       x and y parts were separated, each was changed to an integer type.
       Finally, the x and y components were concatenated and appended to
       the list of points.

Once all components of kmeans.txt were read into the program and stored,
there were a couple of other setup steps necessary. Specifically, a few
lists were created for the calculations to store outputs.

    1. A nested list was created to hold each of the four clusters. In
       each nested list, the points closest to the centroid in that list
       were stored. For example, if centroid 0 had 12 points that were
       closest to it, 'cluster[0]' would have those 12 points appended
       to it.

    2. A list containing the length of each of the clusters from the
       prior iteration was setup. This stored the prior iteration's
       cluster lengths to compare to the new iteration's cluster
       lengths as a way to determine if clusters were changing.

    3. A list was created to store the new length of the clusters.

    4. The list 'distances' was created to store nested lists; for
       each iteration, a list containing the distances of each point
       from each of the four clusters was appended to this list.

    5. A variable 'itr' was created to count the number of times
       the clusters were changing size. Essentially, it represented
       the number of iterations necessary to reach stability.

Calculations
Several calculations were made in an iterative process to create the
four clusters. To begin, a 'for' loop was initialized to keep the
calculations going for a specified number of iterations. Here, the
number of iterations was specified in the kmeans.txt file as 50. The
calculations that followed were:

    1. A 'for' loop was created to iterate through each point in the
       list 'points'. The first calculation was created to find the
       distance of each point from each of the four centroids.
       To accomplish this, one point was taken at a time and the
       distance from that one point was calculated from each of the
       four centroids. To access the centroids x,y coordinates from
       the list 'points', a 'for' loop was created and a variable,
       'cluster', was initialized to contain the index value . From
       there, the x,y coordinates of the centroid could be pulled
       and used in the distance calculation. After the distance was
       calculated for one point and one centroid, it was appended to
       a temporary list, 'distance'. After all four distances were
       calculated for one point to each of the centroids, the 'distance'
       list was appended to 'distances', which held all the distances
       for each iteration. By doing this, each point's distance from
       each of the four centroids over all 50 iterations were
       catalogued and could be pulled easily.

    2. Within the first 'for' loop iterating through each point in the
       list 'points', each point was then assigned to a cluster. To
       determine which centroid, and thus which cluster, a point
       was closest to, the minimum of the four calculated distances
       from above was found. Using 'if/elif' logic, if the minimum
       value had the same index location as a cluster (ranging from
       0 to 3), and thus the same location as a centroid, it was
       appended to that cluster.

    3. After each point was assigned to a cluster, the new length of
       each cluster was calculated. This was accomplished by
       calculating the length of each cluster using 'len()'. A 'for'
       loop was initialized to calculate the length of each of the
       four clusters. The new lengths were then stored in the list
       'new_length'. If the new lengths of each cluster were not
       equal to the prior lengths, that is, if stability was not
       achieved, the variable 'itr' was incremented by one. Finally,
       the new lengths calculated became the 'prior_length' for the
       next round of iterations, and the new_lengths list was cleared.

    4. The next step was to calculate the new positions of each centroid
       by taking the average of all the x and y coordinates of each
       cluster. Several temporary lists were created:

            i. A list to store all the x-coordinates for each cluster
           ii. A list to store the average x-coordinate for each cluster
          iii. A list to store all the y-coordinates for each cluster
           iv. A list to store the average y-coordinate for each cluster
            v. A list to store the concatenated x,y coordinate for each
               new centroid

       To calculate the new centroid positions, a nest 'for' loop was
       structured to pull the x and y values of each point in each
       cluster. Then, the averages of each cluster's x an y values
       was calculated and appended to each respective 'averages' list.
       Finally, the x,y values were concatenated and stored in the list
       'new_centroids.'

    5. Once the new locations of each centroid was calculated, 'if/else'
       logic updated each centroid's location in the list 'points' with
       the new locations calculated in the prior step.

    6. Finally, the lists 'clusters' and 'distances' were emptied for the
       next round of iterations except for the final round of iterations.

Question: This implementation is inefficient for a number of reasons, the first
           of which is the fact that we’re “randomly” selecting the initial
           points for our centroid which means our solution may not be optimal.
           Another reason is that the outlined approach loops the number of
           times specified in the input file, even if stability is achieved
           before the maximum number of iterations has been reached (this
           dataset converges in just 7 iterations though we continue to loop
           the full 50 times). How would you modify your code so that it
           would not needlessly recompute the clusters once the clusters
           stabilize?

Answer: Instead of beginning with 'for i in range(N)', I would begin with 'while
        True' so the code would continue to run until something in the code is
        either falsy or results in a 'break'. After line 71, I would add an 'else'
        with the result 'break'. Effectively, when the current length of the
        clusters is equal to the length of the clusters in the prior iteration,
        the loop breaks and prints the results. I would also need to tweak line
        106 where I empty the lists 'clusters' and 'distances' because it
        currently relies on the use of 'i' in the first 'for' loop, which would
        be gone. Instead, I would remove the 'if' statement all together. Since
        my code would break once stability is reached, and this condition lies
        after the 'break', the lists would not be cleared and my print statements
        would be executed normally.
