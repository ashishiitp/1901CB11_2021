def output_by_subject():
 with open('regtable_old.csv', 'r') as fileregtable:   
    for row in fileregtable:
        words = row.strip().split(',')
        file = open("./output_by_subject/"+words[3]+".csv", "w")
        file.write("rollno,")
        file.write("register_sem,")
        file.write("subno,")
        file.write("sub_type\n")
        with open('regtable_old.csv','r') as f:
            for line in f:
                word=line.split(',')
                if word[3]==words[3]:
                    file.write(word[0]+",")
                    file.write(word[1]+",")
                    file.write(word[3]+",")
                    file.write(word[8])

 return  

def output_individual_roll():
  with open('regtable_old.csv', 'r') as fileregtable: 
    for row in fileregtable:
        words = row.strip().split(',')
        file = open("./output_individual_roll/"+words[0]+".csv", "w")
        file.write("rollno,")
        file.write("register_sem,")
        file.write("subno,")
        file.write("sub_type\n")
        with open('regtable_old.csv','r') as f:
            for line in f:
                word=line.split(',')
                if word[0]==words[0]:
                    file.write(word[0]+",")
                    file.write(word[1]+",")
                    file.write(word[3]+",")
                    file.write(word[8])
    return

output_by_subject()
output_individual_roll()   
