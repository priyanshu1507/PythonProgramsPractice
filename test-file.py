from datetime import datetime

todayDate = datetime.now()
todayTime = datetime.now()

newTodayDate = todayDate.strftime("%d/%m/%y")
newTodayTime = todayTime.strftime("%H:%M")



# My name is Priyanshu and today date is - 21/08/2023 16:58:24

# Write the timestamp to a file
with open('D:\Testing\output.txt', 'w') as f: #D:\Testing\output.txt is a file location 
    f.write(f'My name is Priyanshu and today date is - : {newTodayDate , newTodayTime}\n')
print(f'Current Timestamp: {newTodayDate, newTodayTime}')
#print("My name is Priyanshu and today date is - ", newTodayDate )
   