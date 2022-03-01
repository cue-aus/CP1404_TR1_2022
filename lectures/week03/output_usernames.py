csv_file = "cp1111.csv"


def main():
    try:
        infile = open(csv_file, 'r')  # r: reading, w: writing
        num_of_usernames = 0
        for line in infile:
            num_of_usernames += 1
            temp_list = line.strip().split(',')
            # print(temp_list)
            print(temp_list[2])
        infile.close()
        print("{} usernames from {}".format(num_of_usernames, csv_file))
    except IOError as err:
        print("I/O error: {0}".format(err))


# Start the program
main()
