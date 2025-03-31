package com.leetcode25;

/**
 * Problem:
The task is to convert a string into a zigzag pattern on a given number of rows, and then read the string line by line from top to bottom.

Example:
Input:

java
Copy
s = "PAYPALISHIRING", numRows = 3
Output:

arduino
Copy
"PAHNAPLSIIGYIR"
Solution Explanation:
Approach:

We traverse the string, placing each character at its appropriate position in a zigzag pattern.

The zigzag pattern alternates between moving down the rows and moving up the rows.

We simulate this by using an array of strings to represent each row of the zigzag.

Once the characters are placed in the rows, we simply concatenate them to get the result.

Steps:

We start by creating an array of strings, one for each row.

We move down the rows when we are writing characters in the downward direction, and we move up once we reach the last row.

Finally, we join all the rows together and return the final result.

xplanation:
Edge Case:

If numRows == 1 or numRows >= s.length(), there's no real zigzag to be formed, so the string is returned as is.

StringBuilder Array:

We create an array of StringBuilder objects to represent each row of the zigzag pattern.

Traverse and Fill Rows:

We loop through each character in the string, and depending on the direction (down or up), we add the character to the appropriate row in the rows array.

Direction Switching:

If we reach the first or last row, we toggle the direction (goingDown flag).

Build the Result:

After filling up all the rows, we concatenate the contents of all rows to get the final string.

Time and Space Complexity:
Time Complexity: O(n), where n is the length of the string. We only traverse the string once and process each character.

Space Complexity: O(n), as we are using an array of StringBuilder to store the characters for each row.

Example:
Input: "PAYPALISHIRING", numRows = 3

Output:

arduino
Copy
"PAHNAPLSIIGYIR"
In the zigzag pattern for numRows = 3, the characters are arranged as follows:

css
Copy
P   A   H   N
A P L S I I G
Y   I   R
And reading them row by row gives the output "PAHNAPLSIIGYIR".
 * 
 * 
 * 
 * 
 * 
 */



public class ZigZag6 {

    public String convert(String s, int numRows) {
        // Edge case: If there's only one row or no rows, return the string as it is
        if (numRows == 1 || numRows >= s.length()) {
            return s;
        }

        // Create an array to store strings for each row
        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        // Current position in the row
        int currentRow = 0;
        // Direction flag, true means down, false means up
        boolean goingDown = false;

        // Traverse the string and append characters to the appropriate row
        for (char c : s.toCharArray()) {
            rows[currentRow].append(c);

            // Change direction if we reach the top or bottom row
            if (currentRow == 0 || currentRow == numRows - 1) {
                goingDown = !goingDown;
            }

            // Move up or down
            currentRow += goingDown ? 1 : -1;
        }

        // Build the final string by combining all rows
        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }

    public static void main(String[] args) {
        ZigZag6 solution = new ZigZag6();
        
        // Example test case
        String input = "PAYPALISHIRING";
        int numRows = 3;
        String result = solution.convert(input, numRows);
        
        System.out.println("Zigzag Conversion: " + result); // Output: "PAHNAPLSIIGYIR"
    }
}
