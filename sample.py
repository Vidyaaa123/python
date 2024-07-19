#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    number = int(input("Enter a number: "))
    result = factorial(number)
    print(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()

