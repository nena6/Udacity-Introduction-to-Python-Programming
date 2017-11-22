 # Define the remove_duplicates function
def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target

print(remove_duplicates([1,2,3,4]))

#Using sets

def remove_duplicates(source):
    target_set=set(source)

    return target_set

print(remove_duplicates([1,2,3,4]))
