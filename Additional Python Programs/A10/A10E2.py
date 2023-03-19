def remove_str_from_list(list_of_str, str_to_remove, case_sensitive=True, count=1):
    index=0
    num_of_instances_removed=0
    for i in list_of_str:
        if i==str_to_remove and count>0:
            list_of_str.pop(index)
            count-=1
            num_of_instances_removed+=1
        elif i.lower()==str_to_remove.lower() and count>0 and case_sensitive==False:
            list_of_str.pop(index)
            count-=1
            num_of_instances_removed+=1
        index+=1
    return num_of_instances_removed
zoo=['Ape', 'Bee', 'Ape', 'Cat', 'Ape', 'Dog', 'Ewe', 'ape', 'Fox']
print(remove_str_from_list(zoo, 'ape', False, len(zoo)))