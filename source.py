import csv
from statistics import mean
def calculate_averages(input_file_name,output_file_name):
    with open('/tmp/source.csv') as f:
        reader=csv.reader(f)
        for row in reader:
            name=row[0]
            
            grades_mean=list()
            for grades in row[1:]:
                grades_mean.append(int(grades))
                


#def calculate_sorted_averages(input_file_name,output_file_name):


#def calculate_three_best(input_file_name,output_file_name):


#def calculate_three_worst(input_file_name,output_file_name):


#def calculate_average_of_averages(input_file_name,output_file_name):