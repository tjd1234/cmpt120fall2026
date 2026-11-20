# q4_sol.py

out_of = int(input('What was the test out of? '))
score = float(input('What was your score? '))
percentage = 100 * (score / out_of)

print(f'Score: {percentage:.1f}%')
