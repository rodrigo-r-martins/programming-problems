/*
- FIND PAIRS WITH JAVA

Define a function that finds a pair-value in an array that when we sum those values result in the given target value.
Also it should return a String with those values.

Example: 
array = [1, 3, 5, 6, 8, 20, 11]
target = 8
It should return: 3 and 5 (as String)
*/

class Find_pairs {
	static String find_pairs(int[] values, int target) {
	   for (int value : values) {
		  for (int val : values) {
			 if (value+val == target) {
				return Integer.toString(value) + " and " + Integer.toString(val);
			 }
		  }
	   }
	   return "no pairs value";
	}
 
	public static void main(String[] args) {
	   int[] values = {14, 13, 6, 7, 8, 10, 1, 2};
	   System.out.println(find_pairs(values, 3));
	}
 }