import java.util.stream.IntStream;
class Main {
    public static void main(String[] args) {
        String input="ram is a java developer";
        String vowels="aeiouAEIOU";
        IntStream.range(0,input.length())
          .filter(i->vowels.indexOf(input.charAt(i))!=-1)
          .forEach(i->System.out.println("vowel"+ input.charAt(i)+" found atindex:"+i));
    }
}
