def divide_numbers(numerator,denominator):
    """
divide two numbers and return the result.

Parameters:
numerator(float):The numerator of the division.
denominator(float):The denominator of the division. Must not be zero.

Return:
float:The result of the division.

Raises:
ValueError:If the denominator is zero.
"""
    if denominator==0:
        raise ValurError("Denominator must not be zero.")
    return numerator/denominator
print("This code is written and executed by Anajli_0231BCA188")
