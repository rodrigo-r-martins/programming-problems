"""
- CALCULATE EARNINGS WITH PYTHON

Suppose an individual is taxed 30% if earnings for a given week are > = $2,000. If earnings land < $2,000 for the week, the individual is taxed at a lower rate of 15%.

For example, if an individual earns $55/hour and works for 40 hours, the function should return: 
•	Pre-tax earnings were 55*40 = $2,200 for the week. 
•	Post-tax earnings were $2,200*.7 (since we fall in higher tax bracket here) = $1,540 for the week
"""

def calculate_earnings(earnings_per_hour, hours_worked):

   pre_tax = earnings_per_hour * hours_worked
   
   if pre_tax >= 2000:
      post_tax = pre_tax * .7
   else:
      post_tax = pre_tax * .85

   return f'{float(post_tax):.2f}'


print(calculate_earnings(55, 40))