class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        from collections import defaultdict

        a_len = len(A)
        b_len = len(B)
        if a_len > b_len:
            return 0

        # Initialize frequency array for string A
        a_frequency = [0] * 26
        for char in A:
            a_frequency[ord(char) - ord('a')] += 1
        
        # Initialize frequency array for the first window of size a_len in B
        current_window_frequency = [0] * 26
        for i in range(a_len):
            current_window_frequency[ord(B[i]) - ord('a')] += 1

        result = 0
        # Check if the first window matches the frequency of A
        if current_window_frequency == a_frequency:
            result += 1

        # Slide the window over B
        for i in range(a_len, b_len):
            # Add the new character to the current window frequency
            current_window_frequency[ord(B[i]) - ord('a')] += 1
            # Remove the character that is no longer in the window
            current_window_frequency[ord(B[i - a_len]) - ord('a')] -= 1

            # Check if the current window matches the frequency of A
            if current_window_frequency == a_frequency:
                result += 1

        return result

# Example usage
solution = Solution()
A = "aca"
B = "acaa"
A = "abc"
B = "abcbacabc"
result = solution.solve(A, B)
print(result)  # Output should be 2
