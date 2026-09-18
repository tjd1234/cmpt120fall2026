# test_score.py

#What was the test out of? 34
#What was your score? 22.5
#Score: 66.2%

out_of = int(input('What was the test out of? '))
score = float(input('What was your score? '))

percent = 100 * score / out_of

print(f'Score: {percent:.1f}%')
