'''
Implement a program to check whether the given year is leap year or not.

Input Format

Read year value as an integer from the user.

Constraints

Year>0
Leap Year: It is exactly divisible by 4 except for century year, if it is a century year then it must be divisible by 400.
'''

def isLeapYear(year):
   return (year %4 ==0 and year%100 !=0) or (year%400==0)

year = int(input())
if (isLeapYear(year)):
    print("True")
else:
    print("False")

# implemented on C#
'''
static void Main(string[] args)
{
    Console.Write("Enter a year: ");
    int year = Convert.ToInt32(Console.ReadLine());
    if (isLeapYear(year)) Console.WriteLine($"{year} is a leap year.");
    else Console.WriteLine($"{year} is a not leap year.");
}
static bool isLeapYear(int year) {
    // Check the leap year conditions
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
    {
        return true;
    }
    else
    {
        return false;
    }
}
Console.ReadKey();
'''