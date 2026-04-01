class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""

        # Dictionaries to keep track of character counts
        count_t = {}
        window = {}

        # Populate the target dictionary
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # 'need' is the number of unique characters in t we must match
        have, need = 0, len(count_t)
        
        # Track the best window: [left_index, right_index], and its minimum length
        res, res_len = [-1, -1], float("infinity")
        l = 0

        # Expand the window by moving the right pointer
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # If the current character is in 't' and we hit the exact frequency needed, increment 'have'
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # Shrink the window from the left as long as it remains valid
            while have == need:
                # Update our minimum window result if this one is smaller
                window_size = r - l + 1
                if window_size < res_len:
                    res = [l, r]
                    res_len = window_size

                # Remove the left character from our window to shrink it
                left_char = s[l]
                window[left_char] -= 1
                
                # If we removed a character that was crucial for 't', our window is no longer valid
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                
                # Move the left pointer forward
                l += 1

        # Return the substring using our saved indices
        left_index, right_index = res
        return s[left_index : right_index + 1] if res_len != float("infinity") else ""