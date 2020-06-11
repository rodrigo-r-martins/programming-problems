/*
- CALCULATE EARNINGS WITH JAVA

Suppose an individual is taxed 30% if earnings for a given week are > = $2,000. If earnings land < $2,000 for the week, the individual is taxed at a lower rate of 15%.

For example, if an individual earns $55/hour and works for 40 hours, the function should return: 
•	Pre-tax earnings were 55*40 = $2,200 for the week. 
•	Post-tax earnings were $2,200*.7 (since we fall in higher tax bracket here) = $1,540 for the week
*/

public class CalculateEarnings {
   
   static double calc_earning(int earning_per_hour, int hours_worked) {
      int pre_tax = earning_per_hour * hours_worked;
      double post_tax;

      if (pre_tax >= 2000) {
         post_tax = pre_tax * .70;
      } else {
         post_tax = pre_tax * .85;
      }

      return post_tax;
   }

   public static void main(String[] args) {
      System.out.println(calc_earning(55, 40));
   }
}