def swap_string(first_string, second_string):
    first_list_string = list(first_string)
    second_list_string = list(second_string)

    for index in range(len(first_string)):
        temp = first_list_string[index]
        first_list_string[index] = second_list_string[index]
        second_list_string[index] = temp

        if index > 0: break

    first_to_string = "".join(first_list_string)
    second_to_string = "".join(second_list_string)

    function_output = first_to_string + " " + second_to_string


    return function_output


