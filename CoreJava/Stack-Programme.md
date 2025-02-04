import java.util.Stack;

public class ExpressionEvaluator {

    public static int evaluateExpression(String expression) {
        Stack<Integer> values = new Stack<>();
        Stack<Character> operators = new Stack<>();
        
        for (int i = 0; i < expression.length(); i++) {
            char currentChar = expression.charAt(i);
            
            // If the character is a digit, push it to the values stack
            if (Character.isDigit(currentChar)) {
                values.push(currentChar - '0');
            } 
            // If the character is an operator, check precedence and apply
            else if (currentChar == '+' || currentChar == '*') {
                // Apply operators with higher precedence first
                while (!operators.isEmpty() && hasPrecedence(currentChar, operators.peek())) {
                    char operator = operators.pop();  // Pop operator
                    applyOperator(values, operator);  // Apply operator
                }
                operators.push(currentChar);  // Push the current operator onto the stack
            }
        }
        
        // Apply remaining operators
        while (!operators.isEmpty()) {
            char operator = operators.pop();  // Pop the operator
            applyOperator(values, operator);  // Apply the operator
        }
        
        return values.pop();  // The result is the last value in the stack
    }

    // Function to apply the operator
    private static void applyOperator(Stack<Integer> values, char operator) {
        int b = values.pop();  // Pop the second operand
        int a = values.pop();  // Pop the first operand
        
        switch (operator) {
            case '+':
                values.push(a + b);  // Push the result of a + b
                break;
            case '*':
                values.push(a * b);  // Push the result of a * b
                break;
        }
    }

    // Function to check if the current operator has precedence over the previous one
    private static boolean hasPrecedence(char currentOperator, char prevOperator) {
        return (prevOperator == '*' && (currentOperator == '+' || currentOperator == '*'));
    }

    public static void main(String[] args) {
        String expression = "3+2*2";
        System.out.println("Result: " + evaluateExpression(expression));  // Output: 7
    }
}
