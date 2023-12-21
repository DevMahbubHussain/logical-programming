'''
Given an integer n, perform the following conditional actions,
If n is odd, print weird,
If n is even and in the inclusive range of 2 to 5, print not weird,
If n is even and in the inclusive range 6 to 20, print weird,
If n is even and greater than 20, print not weird.

Input Format

An integer value from the user.

Constraints

1<=n<=100

Output Format

Weird or Not Weird

'''

n = int(input())
if n>=1 and n<=100:
    if n%2!=0:
        print("Weird")
    else:
        if n>=2 and n<=6:
            print("Not Weird")
        elif n>=6 and n<=20:
            print("Weird")
        else:
            print("Not Weird")

'''
implemented on C#
int n = Convert.ToInt32(Console.ReadLine());
if (n >= 1 && n <= 100)
{
    if(n %2 != 0 || (n>=6 && n<=20))
    {
        Console.WriteLine("Weird");
    }
    else
    {
        Console.WriteLine("Not  Weird");
    }
}

'''