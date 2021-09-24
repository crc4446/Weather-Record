def write_data(fileName):
#DESCRIPTION: Prompts user to input month name/rainfall until user enters xxx to stop.
#Writes data to external device
#Close file
#PARAMETERS: The file name
#RETURN: none
    fileOut = open(fileName, 'w')
    month = input('Enter the month. ')
    rainfall = int(input('How much rain fell in {} '.format(month)))
    fileOut.write(month + " ")
    fileOut.write(str(rainfall))
    while (month != "xxx"):
        month = input('Enter the next month. Enter xxx to quit ')
        if (month != "xxx"):
            fileOut.write('\n'+ month + " ")
            rainfall = int(input('How much rain fell in {} '.format(month)))
            fileOut.write(str(rainfall))
        else:
            break

    fileOut.close()



def get_data(fileName):
#DESCRIPTION: Reads data from file, populates two lists (months name/rainfall)
#PARAMETERS: file name to be read
#RETURN: Both lists to main function
    months = []
    rainfalls = []
    with open(fileName, 'r') as file:
        for line in file:
            for word in line.split():
                if (word.isnumeric()==False):
                    months.append(word)
                    #print(word)
                if (word.isnumeric()):
                    rainfalls.append(word)
                    #print(word)
    return (months, rainfalls)
                


def print_list(months, rainfalls):
#DESCRIPTION: Prints values for each month name/rainfall side-by-side 2 tab spaces
#PARAMETERS: Both lists
#RETURN: none
    for x in range(len(months)):
        print("{}{:18.2f}".format(months[x], (int(rainfalls[x]))))



def search_month(months, rainfalls):
#DESCRIPTION: Checks for month in list, if not in list prompts user to enter another month. ("The rainfall for *month* is *rainfall*")
#PARAMETERS: Both lists
#RETURN: none
    mon = input("What month are you interested in? ")
    flag = True
    while (flag == True):
        for m in range(len(months)):
            if months[m] == mon:
                index = months.index(mon)
                flag = False
                break
        if (flag == True):
            mon = input("What month are you interested in? ")
    if (flag == False):
        print('The rainfall for {} was {}'.format(mon, rainfalls[index]))



def print_high_low(months, rainfalls):#Use index(), max(), min()
#DESCRIPTION: Prints the month with the highest rainfall and the month with the lowest rainfall.
#PARAMETERS: Both lists
#RETURN: none
    maximum = max(rainfalls)
    minimum = min(rainfalls)
    indexMax = rainfalls.index(maximum)
    indexMin = rainfalls.index(minimum)
    print('{} had the highest rainfall with {:0.1f} inches and {} had the lowest rainfall with {:0.1f} inches.'.format(months[indexMax], (int(maximum)), months[indexMin], (int(minimum))))



def main():
    select = input("Enter: C to create a new file, V to view the data, S to see a month, H to see the highest/lowest.")
    fileName = input("What is the name of the file you are working on? ")
    if select == 'c':
        write_data(fileName)
    elif select == 'v':
        months, rainfalls = get_data(fileName)
        print_list(months, rainfalls)
    elif select == 'h':
        months, rainfalls = get_data(fileName)
        print_high_low(months, rainfalls)
    elif select == 's':
        months, rainfalls = get_data(fileName)
        search_month(months, rainfalls)
    
main()