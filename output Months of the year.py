#Michael A Walker
#Homework 1
#Months of the Year
print('programming 3:-')

MONTH = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
         'Sep', 'Oct', 'Nov', 'Dec',]
def main():
    month_rain =[0.0]*12
    print('Input the amount of rainfall for each month.')
    for i in range (12):
        print(MONTH[i],':', end='')
        month_rain[i] = float(input())
    print('details of rainfall')
    print('---------------------')
    show_details(month_rain)
    display_summary(month_rain, MONTH)

def show_details (month_rain ):
    index =0
    while index <len(month_rain ):
        print(MONTH [index], ':', format(month_rain[index], '.2f'))
        index +=1
        
def display_summary (month_rain , MONTH):
    total_rainfall = sum(month_rain)
    avg_rainfall = sum(month_rain)/len(MONTH)
    highest = max(month_rain)
    rainfall = month_rain.index(max(month_rain))
    
    print('summary of rainfall')
    print('----------------------')
    print ('total rainfall: ',format(total_rainfall,'.2f'))
    print ('average rainfall: ' ,format(avg_rainfall, '.2f'))
    print ('highest rainfall: ' ,format(highest,'.2f'))
    print ('month of highest',MONTH[rainfall])

main()
            
     
    
                                     


    
    
        
        
    
                                    
