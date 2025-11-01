import unittest
import re

# We will not check for valid rolls.
# We will not check for correct number of rolls and frames.
# We will not provide scores for intermediate frames.

class BowlingTest(unittest.TestCase):

    def test_result_of_no_pins(self):
        self.assertEqual(calculate_total_score("-"), 0)

    def test_result_of_zero_points_half_frame(self):
        self.assertEqual(calculate_total_score("-2"), 2)
    
    def test_result_of_strike(self):
        self.assertEqual(calculate_total_score("X"), 10)
    
    def test_result_of_spare(self):
        self.assertEqual(calculate_total_score("4/"), 10)
    
    def test_result_of_open_frame(self):
        self.assertEqual(calculate_total_score("45"), 9)

    # # test of zero points - remove empty score - add to make invalid 
    # def test_result_of_two_frames(self):
    #      self.assertEqual('X 2/', 20)
    

def calculate_total_score(score):
  
    if score == "":
        score = 0
    if len(score) > 1:
        score = list(score)
    if '-' in score:
        score = ['0' if x == '-' else x for x in score]
    if 'X' in score:
        score = ['10' if x == 'X' else x for x in score]
    for i, char in enumerate(score):
        if '/' == score[i]: 
            score = score[:i-1] + ['10'] + score[i+1:]
    

    return sum(list(map(int, score)))


if __name__ == '__main__':
    unittest.main()


#  'X, 45, 4/, 32, X, 45, 4/, 32, X, 11'
#  is the next step to have ten frames? which is a valid input, and then rework the logic to start the rules of bowling? 
#  or is there a simpler way!? 

# Next step - DRY, lets move out the strike and spare into own functions and then call that 


    # score = score.split()
    # print(score)
    # for index, point in enumerate(score):
    #      if point == 'X' or '/' in point:
    #         score[index] = '10'
    
    # score = [int(x) for x in score]
    # score = sum(score)
    # print(score)
    # return score
    

