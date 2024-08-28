import numpy as np

activators_col_repressors_col = [
    # in each array, the left column represent the activators state,
    # corresponding to the two left circles in each graph at the table.

    # in each array, the right column represent the repressors state,
    # corresponding to the two right circles in each graph at the table.

    # 1 - means present, 0 - means not present

    np.array([[0, 0], [0, 0]]), # All activators and repressors aren't present.
    np.array([[1, 0], [0, 0]]), # Some but not all of the activators are present. None of the repressors are present.
    np.array([[1, 0], [1, 0]]), # All of the activators are present. None of the repressors are present.
    np.array([[0, 1], [0, 0]]), # Some but not all of the repressors are present. None of the activators are present.
    np.array([[1, 1], [0, 0]]), # Some but not all the repressors, as well as some but not all the activators, are present.
    np.array([[1, 1], [1, 0]]), # Some but not all of the repressors are present. All of the activators are present.
    np.array([[0, 1], [0, 1]]), # All of the repressors are present. None of the activators are present.
    np.array([[1, 1], [0, 1]]), # Some but not all of the activators are present. All of the repressors are present.
    np.array([[1, 1], [1, 1]]) # All activators and repressors are present.
]

# function to generates all possible combinations to make a list of a given length using just of 0 and 1
def generate_possible_functions(length,sub_list=[]):
    if length == 0:
        return [sub_list]
    return (generate_possible_functions(length-1, sub_list+[0]) +
            generate_possible_functions(length-1, sub_list+[1]))

def find_monotonic_functions(possible_functions,activators_col_repressors_col):
    # Initialize monotonic function list
    monotonic_functions =[]

    # checking which functions are monotonic:
    for func in possible_functions:
        monotonic = True

        # iterating over the each "box"
        for i in range(len(activators_col_repressors_col)):

            if func[i]==1: # if regulated component is active at state i

                # we need to check that if one of the activators switches from inactive to active, the regulated
                # component still remains active
                for k in range(len(activators_col_repressors_col)):

                    # getting state of the activators and repressors at column i and column k
                    state1 = activators_col_repressors_col[i]
                    state2 = activators_col_repressors_col[k]

                    # if an activator switches from inactive to active
                    if (state2[0][0]+state2[1][0])>(state1[0][0]+state1[1][0]):

                        # repressors must remain unchanged so it won't affect the component
                        if (state2[0][1]+state2[1][1])==(state1[0][1]+state1[1][1]):

                            # check if the regulated component remain active
                            if func[k] != 1:
                                monotonic = False # if it is inactive, we can infer the function is not monotonic
                                break


            else: # if regulated component is inactive at state i

                # we need to check that if one of the repressors switches from inactive to active, the regulated
                # component remains inactive.
                for k in range(len(activators_col_repressors_col)):

                    # getting state of the activators and repressors at column i and column k
                    state1 = activators_col_repressors_col[i]
                    state2 = activators_col_repressors_col[k]

                    # if an activator switches from inactive to active
                    if (state2[0][1]+state2[1][1])>(state1[0][1]+state1[1][1]):

                        # activators must remain unchanged so it won't affect the component
                        if (state2[0][0]+state2[1][0])==(state1[0][0]+state1[1][0]):

                            # check if the regulated component remain inactive
                            if func[k] != 0:
                                monotonic = False # if it is active, we can infer the function is not monotonic
                                break

        if monotonic == True:
            monotonic_functions.append(func)

    return monotonic_functions


def main():

    # get possible functions
    possible_functions = generate_possible_functions(len(activators_col_repressors_col))

    # Remove uninteresting cases
    inactive = []
    active = []
    for i in range(len(activators_col_repressors_col)):
        inactive.append(0)
        active.append(1)
    possible_functions.remove(
        inactive)  # case were it is always inactive, regardless of the state of the activators and repressors
    possible_functions.remove(
        active)  # case were it is always inactive, regardless of the state of the activators and repressors

    # find monotonic functions
    monotonic_functions = find_monotonic_functions(possible_functions, activators_col_repressors_col)

    # print monotonic functions
    for func in monotonic_functions:
        print(func)

if __name__ == "__main__":
    main()
