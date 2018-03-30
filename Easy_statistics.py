# Create an empty list
num = []
while True:
    #Ask user for number to add to list
    try:
        x = int(input('Enter a score to add to list or something else to stop: '))
        # Add number entered to list
        num.append(int(x))
        print (num)
    # If user enters something else, end list and continue with Arithmetic 
    except:
        print ('List of scores entered: ', num)
        print ('Entered ', len(num), 'scores')
        print ('They sum to ', sum(num))
        print ('Minimum score is ', min(num))
        print ('Maximum score is ', max(num))
        mean = (sum(num))/float(len(num))
        print ('The mean of the scores is: ', mean)

        print ('Their squares: ')
        # Iterate through the number list
        for i in num:
            print ('The square of ', i, 'is ', (i ** 2))

        # Calculate variance for the sample data
        values = 0
        for i in num:
            values += (i-mean)**2
            var = values/(len(num)-1)
        print ('The variance for the sample data is ', var)

        # Calculate the standard deviation
        std_dv = var ** 0.5
        print ('The standard deviation is ', std_dv)
        
        break
