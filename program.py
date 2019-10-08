#declare the point of this program file. ie ( what is it going to do?)
# the point is to define a function that returns the number of entries in the dataset and the average charge after filtering

#define the function that Is going to do the actual calculation of the task
#Each of the arguements are going to be criteria that are used to filter the data. For example,
# he will provide a filename, a minimium age, a maximum age and the region(s). Based on what those values are, your function
# should return only the rows with columns that match the search terms or 'arguements'.
#include the function name and the parameters that the prof is going to check against.(they are called parameters when in the function, and arguements when they are actually being called)
def compute_avg_charges(filename, min_age, max_age, regions):
    #open the CSV file using a nested function. (did this to keep things neat)
    def read_csv(csv_file):
        #create an empty list to eventually put the data into
        data = []
        #actually open the file with read only permissions using the variable f
        with open(filename, 'r') as f:


        # create a list of rows in the file
            rows = f.readlines()
        #eliminate the first row (age,sex,bmi,children,smoker,region,charges) so that we can do calculations
            rows = rows[1:]
        # strip white-space and newlines
            rows = list(map(lambda x:x.strip(), rows))
        #start a loop to make columns
            for row in rows:

            # further split each row into columns assuming delimiter is comma
                row = row.split(',')

            # append to data-frame our new row-object with columns
                data.append(row)
            #return the data from the readcsv function
            return data



# invoke our sorting function using the filename parameter
    data = read_csv(filename)
#create a new blank list so we can put our filtered data into somewhere new for analysis
    x = []
#this is defining the count which will be used to get the average of charges (avg = sum of data / total occurances)
    count = 0
    #loop through the dataset
    for i in data:
#an if statement to filter the age using min / max age and the region arguements
        if (int(i[0]) > min_age) and (int(i[0]) <= max_age) and i[5] == regions:
            
            #I added the filtered the results to the x list I created a few lines up
            x.append(float(i[6]))
            
            #this increments the count by one every iteration of the loop(nessesary to keep track of how many charges are in the dataset)
            count += 1
        
   
        #print the data required
    print('the amount of entries (people) with filter: ' ,count)
    print('average charge with filter: ', sum(x)/count)
    #print('the total amount of entries in the filtered dataset: ', count*7)

#calling the function with random arguements. if the format of the test file does not insert the data like this, we will have to adjust some things.
#comment out the line below before submission, he will probably call the function a different way
compute_avg_charges('insurance.csv',0,60,'southwest')
