filename = 'data.txt'

def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details

def prep_to_write(first_name, last_name, courses):
    full_name = first_name + "," + last_name
    courses = ",".join(courses)
    return full_name + ":" + courses


with open(filename) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, course_details = prep_record(line)
        print(first_name, last_name, course_details)

to_write = prep_to_write(first_name, last_name, course_details)
print(to_write)

recors_to_add = "john,doe:c,ruby,javascript"

# with open(filename, "a+") as to_write:
#     to_write.write(recors_to_add+"\n")

# mashrur,hossain:python,ruby,javascript
# joe,schmo:python,ruby,javascript
# john,schmoe:python,ruby,javascriptjane,doe:c,ruby,javascript
# jane,doe:c,ruby,javascriptjohn,doe:c,ruby,javascript