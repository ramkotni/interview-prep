public class UpperCaseCount {

    public static void main(String[] args) {
        String sentence = "Hello World! This is Java.";

        // Call the method to count uppercase characters
        int upperCaseCount = countUpperCaseCharacters(sentence);

        System.out.println("The sentence contains " + upperCaseCount + " uppercase characters.");
    }

    public static int countUpperCaseCharacters(String sentence) {
        int count = 0;

        // Loop through each character in the sentence
        for (int i = 0; i < sentence.length(); i++) {
            char ch = sentence.charAt(i);

            // Check if the character is uppercase using ASCII values
            if (ch >= 65 && ch <= 90) {
                count++; // Increment count if the character is uppercase
            }
        }

        return count; // Return the total count of uppercase characters
    }
}
