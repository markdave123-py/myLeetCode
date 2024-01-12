def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """

    # Helper function to calculate the sum of squares of digits
    def sum_of_squares_of_digits(num):
        sum_squares = 0
        while num > 0:
            # Extract the last digit of the number
            digit = num % 10
            # Add the square of the digit to the sum
            sum_squares += digit ** 2
            # Remove the last digit from the number
            num //= 10
        return sum_squares

    # Initialize a set to keep track of the sums seen so far
    seen_sums = set()

    # Repeat until we find 1 or detect a cycle
    while n != 1:
        # Calculate the sum of squares of digits for the current number
        n = sum_of_squares_of_digits(n)

        # If the sum is in the set, we have entered a cycle
        if n in seen_sums:
            return False

        # Add the sum to the set
        seen_sums.add(n)

    # If the loop ends, the number is happy (equals 1)
    return True
