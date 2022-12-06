import sys
import statistics
def get_grade_list():
    sys.argv.pop(0)
    for i in range(len(sys.argv)):
            sys.argv[i]=float(sys.argv[i])
    return sys.argv
def calculate_grade_stats(num_list):
    num_list.sort(reverse=True)
    for i in range(len(num_list)):
        if num_list[i]==0:
                num_list.pop(i)
    number_of_grades=len(num_list)
    lowest_grade=num_list[-1]
    highest_grade=num_list[0]
    average=round(statistics.fmean(num_list),1)
    return number_of_grades,lowest_grade,highest_grade,average

def main():
    num_list=get_grade_list()
    data=calculate_grade_stats(num_list)
    print("The grades listed top-to-bottom are: ",end="")
    for i in range(len(num_list)):
        if i==0:
            print(num_list[i],end="")
        else:
            print(end=", ")
            print(num_list[i],end="")
    print("\nThere are",data[0],"data in the list.")
    print("The top grade is",data[2])
    print("The bottom grade is",data[1])
    print("The average grade is",data[3])
main()