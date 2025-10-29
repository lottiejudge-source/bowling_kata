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
    

def calculate_total_score(score):
    if score == "":
        score = '0'
    elif score == 'X':
        score = '10'
    elif '/' in score:
        score = '10'
    elif len(score) >= 2:
       score = sum(list(map(int, score)))
       print(score)
    else :
        score = int(score)

    return int(score)


if __name__ == '__main__':
    unittest.main()


#  'X, 45, 4/, 32, X, 45, 4/, 32' - this equals 92 so ias the next smallest step to get
# then make score logic e,g x == 10 
# next step is to sum score? 


    # score = score.split()
    # print(score)
    # for index, point in enumerate(score):
    #      if point == 'X' or '/' in point:
    #         score[index] = '10'
    
    # score = [int(x) for x in score]
    # score = sum(score)
    # print(score)
    # return score
    

