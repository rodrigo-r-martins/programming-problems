'''
SCHOOL MASCOTS
- Statistics Probability Theory Bayes

Suppose a student poll is taken across three classrooms to decide on a new school mascot.
In classroom A, 50% of students support a penguin mascot, in classroom B, 60% of the students support the penguin mascot, and in classroom C, 35% of the students support the penguin mascot. 
Of the total population of the three classrooms, 40% are members of classroom A, 25% are members of classroom B, and 35% are members of classroom C. 
Given that a student supports the penguin mascot, what is the probability that they are a member of classroom B?

Formula: P(A|B) = P(B|A)*P(A) / P(B)
P(B|A) = percuentual of all students that supports penguin
P(A) = percuentual of all students in classB that supports penguin
P(B) = percentual of all students in classB
'''

# Calculating total support of penguin mascot
support_class_A = 40*50/100
support_class_B = 25*60/100
support_class_C = 35*35/100
print(f'''=== Penguin Support ===
Support of class_A: {support_class_A:.1f}%
Support of class_B: {support_class_B:.1f}%
Support of class_C: {support_class_C:.1f}%''')

percentual_total_students_class_B = 25
total_support = support_class_A + support_class_B + support_class_C
print(f'Penguin support for all classes: {total_support:.1f}%')
print('========================')

# Bayes Theorem
probability_class_B = support_class_B * total_support / percentual_total_students_class_B
print(f'''===== Final Result =====
Probability of being a member of class B: {probability_class_B:.1f}%')
========================''')