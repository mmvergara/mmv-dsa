class Solution:
    def minWindow(self, s, t):
        """
        Approach:
        Use a sliding window technique to find the minimum window substring that contains all characters from t.
        1. Create a dictionary to store the character count of string t.
        2. Initialize variables to track the window and the character count inside the window.
        3. Move the window_end to the right to expand the window and find the first valid substring that contains all characters from t.
        4. Once a valid substring is found, move the window_start to the right to try to shrink the window while keeping all characters from t.
        5. Continue moving both pointers until the end of the string s is reached.
        6. Keep track of the minimum window size and its starting position, and return the minimum window substring.

        :param s: The input string s.
        :param t: The target string t.
        :return: The minimum window substring containing all characters from t, or an empty string if not found.
        """

        # Create a dictionary to store the character count of string t
        target_counts = {}
        for char in t:
            target_counts[char] = target_counts.get(char, 0) + 1

        # Initialize variables to track the window and the character count inside the window
        window_start = 0
        window_end = 0
        min_window_size = float('inf')
        min_window_start = 0
        chars_to_match = len(target_counts)

        while window_end < len(s):
            # Expand the window by moving window_end to the right
            if s[window_end] in target_counts:
                target_counts[s[window_end]] -= 1
                if target_counts[s[window_end]] == 0:
                    chars_to_match -= 1

            window_end += 1

            # Shrink the window by moving window_start to the right
            while chars_to_match == 0:
                if window_end - window_start < min_window_size:
                    min_window_size = window_end - window_start
                    min_window_start = window_start

                if s[window_start] in target_counts:
                    target_counts[s[window_start]] += 1
                    if target_counts[s[window_start]] > 0:
                        chars_to_match += 1

                window_start += 1

        if min_window_size == float('inf'):
            return ""
        else:
            return s[min_window_start:min_window_start + min_window_size]
