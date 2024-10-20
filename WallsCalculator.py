from datetime import date

monthsDays = {0: 0, 1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def convertDaystoNumbers(date):
    days = date[0]
    month = date[1]
    total_days = 0
    for i in range(1, month):
        total_days += monthsDays.get(i)
    total_days += days
    return total_days

def dateDifference(date1, date2, includeCurrentDate):
    end = convertDaystoNumbers(date2)
    start = convertDaystoNumbers(date1)
    if includeCurrentDate:
        return end - start + 1
    else:
        return end - start

def inputParser(stringInput):
    result = []
    day = int(stringInput[0:2])
    month = int(stringInput[3:5])
    if day > 31 or day < 1 or month > 12 or month < 1:
        raise ValueError("Invalid Date.")
    else:
        result.append(day)
        result.append(month)
    return result

def main():
    try:
        timeLeft = None
        currentDate = inputParser(date.today().strftime("%d-%m"))
        updateDate = inputParser("15-12")
        print("Do you want to include today's date in the calculation? (yes/no) ", end="")
        choice = input().strip().lower()
        if choice in ['yes', 'no']:
            include_today = (choice == 'yes')
            timeLeft = dateDifference(currentDate, updateDate, include_today)
        else:
            print("Invalid choice")
        print("How many walls are left to upgrade? ", end="")
        walls = int(input())
        averageperDay=float(walls/timeLeft)
        print("You need to upgrade "+str(averageperDay)+" walls per day before update drops.")
        costMultiplier=4_500_000
        print("You need to farm "+str(int(averageperDay*costMultiplier))+" gold and "+str(int(averageperDay*costMultiplier))+" elixir each day.")
        
    except ValueError as e:
        print(f"An error occurred: {e}")

if __name__=="__main__":
    main()
