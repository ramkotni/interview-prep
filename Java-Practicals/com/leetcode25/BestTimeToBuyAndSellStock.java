package com.leetcode25;

/**
 * The Best Time to Buy and Sell Stock problem is a classic problem where you need to find the maximum profit you can achieve by buying and selling a stock once. You are given an array prices[] where each element represents the price of the stock on that day.

Problem:
Given an array prices where prices[i] is the price of a given stock on the i-th day, you want to determine the maximum profit you can achieve by buying and then selling the stock.

Optimal Approach:
The optimal solution involves a single pass through the prices array while maintaining the minimum price seen so far and the maximum profit possible at each step. This results in an O(n) time complexity solution, where n is the number of elements in the prices array.


 * Explanation:
Initialization:

minPrice is set to Integer.MAX_VALUE to ensure that any price in the array will be less than this value initially.

maxProfit is initialized to 0, because initially, no transactions have been made, so the profit is zero.

Single Pass:

We iterate through the prices array.

For each price:

We check if the current price is less than minPrice. If so, we update minPrice.

We then calculate the profit if we were to sell at the current price (price - minPrice).

If the calculated profit is greater than maxProfit, we update maxProfit.

Final Answer:

After completing the loop, maxProfit contains the maximum profit achievable by buying and selling the stock once.

Time Complexity:
Time Complexity: O(n), where n is the number of days (or length of the prices array). We only loop through the array once.

Space Complexity: O(1), since we are only using a constant amount of extra space (for minPrice and maxProfit).
 * 
 * 
 * Explanation:
Buy on day 2 (price = 1), sell on day 5 (price = 6), profit = 6 - 1 = 5.

This solution is optimal and works efficiently for large inputs!
 * 
 * 
 */




public class BestTimeToBuyAndSellStock {

    public int maxProfit(int[] prices) {
        // If there are no prices or just one price, no transaction can be made.
        if (prices == null || prices.length <= 1) {
            return 0;
        }
        
        int minPrice = Integer.MAX_VALUE;  // To track the minimum price seen so far
        int maxProfit = 0;  // To track the maximum profit we can make
        
        // Traverse through the prices array
        for (int price : prices) {
            // Update the minimum price
            if (price < minPrice) {
                minPrice = price;
            }
            
            // Calculate the profit if we sell at the current price
            int profit = price - minPrice;
            
            // Update the maximum profit
            if (profit > maxProfit) {
                maxProfit = profit;
            }
        }
        
        return maxProfit;
    }

    public static void main(String[] args) {
        BestTimeToBuyAndSellStock solution = new BestTimeToBuyAndSellStock();
        
        // Test the solution with an example
        int[] prices = {7, 1, 5, 3, 6, 4};
        int result = solution.maxProfit(prices);
        
        // Print the result
        System.out.println("Maximum Profit: " + result);
    }
}
