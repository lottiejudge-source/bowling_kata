import unittest

class BowlingTest(unittest.TestCase):

    def test_result_of_no_pins(self):
        self.assertEqual(calculate_total_score(""), 0)
    
    def test_result_of_strike(self):
        self.assertEqual(calculate_total_score("X"), 10)
    
    def test_result_of_spare(self):
        self.assertEqual(calculate_total_score("4/"), 10)
    
    def test_result_of_open_frame(self):
        self.assertEqual(calculate_total_score("45"), 9)

    # test of zero points - remove empty score - add to make invalid 
    def test_result_of_zero_points(self):
        self.assertEqual(calculate_total_score("-2 X"), 2)
    
    # def test_result_of_invalid_frame_length(self):
    #     self.assertEqual()
    

def calculate_total_score(score):

    if score == "":
        score = '0'
    elif score == 'X':
        score = '10'
    elif '/' in score:
        score = '10'
    elif '-' in score:
        score = score.replace('-', '0')
    elif len(score) >= 2:
       score = sum(list(map(int, score)))
       print(score)
   
    else :
        score = int(score)

    return int(score)


if __name__ == '__main__':
    unittest.main()


#  'X, 45, 4/, 32, X, 45, 4/, 32, X, 11'
#  is the next step to have ten frames? which is a valid input, and then rework the logic to start the rules of bowling? 
#  or is there a simpler way!? 



    # score = score.split()
    # print(score)
    # for index, point in enumerate(score):
    #      if point == 'X' or '/' in point:
    #         score[index] = '10'
    
    # score = [int(x) for x in score]
    # score = sum(score)
    # print(score)
    # return score
    

