## /bin/py
## this file is meant to be used to generate distinct usernames from two given input files filled with first and last names
##


import string, random, csv

# Global
first_names_file = 'firstnames.csv'
last_names_file = 'lastnames.csv'
output_file = 'usernames.csv'


# IO
def get_names(first_names_file, last_names_file, output_file):
    # Read first names
    with open(first_names_file, 'r', newline='') as file1:
        reader1 = csv.reader(file1)
        first_names = [row[0] for row in reader1]

    # Read last names
    with open(last_names_file, 'r', newline='') as file2:
        reader2 = csv.reader(file2)
        last_names = [row[0] for row in reader2]

    count = min(len(first_names), len(last_names))

    # Write
    with open(output_file, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        for i in range(count):
            first_name = first_names[i]
            last_name = last_names[i]

            # assigning the names
            result = assign(first_name, last_name)
            if i % 7 == 0: # 7 can be changed acccording to how many cryptic ones are required
                result2 = change_chars(result) 
                writer.writerow([result2.lower()])
            #output to csv
            else:
                writer.writerow([result.lower()])


def assign(fname, lname):
    
    iter = random.choice(range(100))
    match iter: 
        case iter if iter in range(0,5):
            return firstlast(fname,lname)
        case iter if iter in range(5,10):
            return flast(fname,lname)  
        case iter if iter in range(10,15):
            return firstl123(fname,lname)
        case iter if iter in range(15,20):
            return flast123(fname,lname)
        case iter if iter in range(20,25):
            return firstdlast(fname,lname)
        case iter if iter in range(25,30):
            return lastdfirst(fname,lname)
        case iter if iter in range(30,35):
            return fdlast(fname,lname)
        case iter if iter in range(35,40):
            return firstdl(fname,lname)
        case iter if iter in range(40,45):
            return firstdlast123(fname,lname)
        case iter if iter in range(45,50):
            return firstdl123(fname,lname)
        case iter if iter in range(50,55):
            return fulast(fname,lname)
        case iter if iter in range(55,60):
            return firstulast(fname,lname)
        case iter if iter in range(60,65):
            return lastufirst(fname,lname)        
        case iter if iter in range(65,70):
            return fulu123(fname,lname)
        case iter if iter in range(70,75):
            return fulast123(fname,lname)
        case iter if iter in range(75,80):
            return firstul123(fname,lname)
        case iter if iter in range(80,85):
            return novowels(fname,lname)
        case iter if iter in range(85,90):
            return novowels123(fname,lname)
        case iter if iter in range(90,95):
            return altchar(fname,lname)
        case iter if iter in range(95,100):
            return mix(fname,lname)        
        
        # hate this wall of bs
def change_chars(result):
    replaced_string = ""
    count = 0 
    for char in result:
        if char == 'A':
            replaced_string += '4'
        elif char == 'e':
            replaced_string += '3'
        elif char == 'o':
            replaced_string += '0'
        elif char == 'I':
            replaced_string += '1'
        elif char == 'S':
            replaced_string += '5'
        elif char == 'T':
            replaced_string += '7'
        elif char == 'B' or char == 'g':
            replaced_string += '8'
        else:
            replaced_string += char
    print(replaced_string.lower())
    return replaced_string


#### functions for all patterns ####

### ~~ regular usernames ~~ ###
# fnamelname
def firstlast(fname, lname):
    username = ''
    username += fname+lname
    return username
# flname
def flast(fname, lname):
    username = ''
    username += fname[0]+lname
    return username
# fnamel123
def firstl123(fname, lname):
    username = ''
    username += fname+lname[0] + (''.join(random.choice(string.digits) for _ in range(2)))
    return username
# flname123
def flast123(fname, lname):
    username = ''
    username += fname[0]+lname + (''.join(random.choice(string.digits) for _ in range(2)))
    return username


### ~~ dot usernames ~~ ### 
# first.last
def firstdlast(fname, lname):
    username = ''
    username += fname + "." + lname
    return username
# last.first
def lastdfirst(fname, lname):
    username = ''
    username += lname + "." + fname
    return username
# f.last
def fdlast(fname, lname):
    username = ''
    username += fname[0]+'.'+lname
    return username
# first.l
def firstdl(fname, lname):
    username = ''
    username += fname + '.' + lname[0]
    return username

## with numbers
# first.last123
def firstdlast123(fname, lname):
    username = ''
    username += fname + "." + lname + (''.join(random.choice(string.digits) for _ in range(2)))
    return username
# fname.l123
def firstdl123(fname, lname):
    username = ''
    username += fname + '.' + lname[0] + (''.join(random.choice(string.digits) for _ in range(2)))
    return username


### ~~ underscore usernames ~~ ###
# f_lname
def fulast(fname, lname):
    username = ''
    username += fname[0]+ '_' +lname
    return username
# first_last
def firstulast(fname, lname):
    username = ''
    username += fname + "_" + lname
    return username
# last_first
def lastufirst(fname, lname):
    username = ''
    username += lname + "_" + fname
    return username

## underscore numbers
# f123last
def fulu123(fname,lname):
    username = ''
    username += fname[0] + (''.join(random.choice(string.digits) for _ in range(2))) + lname
    return username
# f_lname123
def fulast123(fname, lname):
    username = ''
    username += fname[0]+ '_' +lname + (''.join(random.choice(string.digits) for _ in range(2))) 
    return username
# first_l123
def firstul123(fname, lname):
    username = ''
    username += fname + "_" + lname[0] + (''.join(random.choice(string.digits) for _ in range(2))) 
    return username
    
#fst.lst
def novowels(fname, lname):
    name = fname + "." + lname
    username = ''.join(char for char in name if char.lower() not in 'aeiou')
    return username
#fst_lst
def novowels123(fname, lname):
    name = fname + "." + lname + (''.join(random.choice(string.digits) for _ in range(2)))
    username = ''.join(char for char in name if char.lower() not in 'aeiou')
    return username

### random (open to more pattern suggestions)
#frt.at
def altchar(fname,lname):
    username = fname + "." + lname
    return username[::2]
#first._ls_
def mix(fname, lname):
    username = fname + "." + "_" + lname[::3] + "_"
    return username


if __name__ == "__main__":
    # everything function
    get_names(first_names_file, last_names_file, output_file)

    print(f"usernames have been saved to {output_file}.")