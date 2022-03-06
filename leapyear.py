startyear=int(input ("enter the start year"))
endyear=int(input("enter the end year"))
for year in range(startyear,endyear):
    if (year%4==0 and year%100!=0 or year%400==0):
        print(" leap year is",year)

