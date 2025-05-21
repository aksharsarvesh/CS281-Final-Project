import re
if __name__ == "__main__":
    data = "adult/adult.data"
    test = "adult/adult.test"
    file = open(data, "r")
    out = "data/income_data.csv"
    outfile = open(out, "w+")
    outfile.write("age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,income\n")
    line = file.readline()
    while line != "":
        line = re.sub(r"[. \t\f\r\v]", "", line)
        outfile.write(line)
        line = file.readline()
    file.close()
    file = open(test, "r")
    line = file.readline()
    line = file.readline()
    while line != "":
        line = re.sub(r"[. \t\f\r\v]", "", line)
        outfile.write(line)
        line = file.readline()
        
    file.close()
    outfile.close()