def greedySortingReversals(permutation):
    approxReversalDistance = 0

    for k in range(1, len(permutation) + 1):
        if permutation[k - 1] != k:
            # If the element is not sorted, apply the k-sorting reversal
            k_index = permutation.index(k)
            permutation[k_index:] = [-x for x in reversed(permutation[k_index:])]
            approxReversalDistance += 1

    return approxReversalDistance

# Create the permutation (+100 +99 ... +2 +1)
permutation = list(range(100, 0, -1))

reversal_count = greedySortingReversals(permutation)

print("Number of reversals needed:", reversal_count)
