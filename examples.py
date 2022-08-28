#bad code
def count_unique_values_name_list_with_set(names_list):
    return len(set(names_list))

#better code
def count_unique_values(arr): #using meaningful names
    return len(set(arr))    