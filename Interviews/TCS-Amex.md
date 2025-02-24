/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main
{
	public static void main(String[] args) {
	    int n=5;
        List<List<Integer>> result=new ArrayList<>();
        findcombination(n,new ArrayList<>(),result);
        result.forEach(combination->
              System.out.println(combination.stream().map(String::valueOf)
                                       .collect(Collectors.joining("+"))));
	}
	
	private static void findcombination(int n,List<Integer> tempList,List<List<Integer>> result){
	    if(n==0){
	        result.add(new ArrayList<>(tempList));
	        return;
	    }
	    for(int i=1;i<=n;i++){
	        if(! tempList.isEmpty() && i<tempList.get(tempList.size()-1)){
	            continue;
	        }
	        tempList.add(i);
	        findcombination(n-i,tempList,result);
	        tempList.remove(tempList.size()-1);
	    }
	}
}

============================
