import os
import codecs

test_path = "t0.txt"
result_path = "result0.txt"

testfile = open(test_path, "r")
resultfile = open(result_path , "r")

line = testfile.readline()
correct_data = []
while (line != "") :
    correct_data.append(int(line))
    line = testfile.readline()
correct_data.sort()


line = resultfile.readline()
line = resultfile.readline()
input_data_idx = 0
while (line != "") :
    info = [(i.replace('"' , '')) for i in line.split(",")]
    valid = int(info[5])
    done = int(info[7])
    cur_clock = int(info[1],16)
    n = int(info[2],9)
    if (valid and cur_clock) :
        data = int(info[6],8)
        if not (correct_data[input_data_idx] == data) :
            print(f"Wrong answer : {input_data_idx} {correct_data[input_data_idx]} {data}")
            break
        input_data_idx += 1
    if (done) :
        clock = int(info[8],16)
        if (input_data_idx == n) :
            print("Correct answer")
        else :
            print("Wrong answer")
        print(f"Clock using : {clock}")
        break
    line = resultfile.readline()