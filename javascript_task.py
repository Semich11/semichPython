# Step 01: Convert list to set
# Step 02: Convert list to set
# Step 03: Count the occurrence of each element in the set in the array




# user_input = [1,1,2,3,2]
# user_input = [5,4,5,6,7,6]
def occurrence_count(user_input):

    out_put = {}

    to_set = set(user_input)
    count = 0
    for _ in to_set:
        for i in user_input:
            if _ == i:
                count += 1

        out_put.update({_:count})
        count = 0

    return out_put


print(occurrence_count([1,1,2,3,2]))

