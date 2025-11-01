import unittest
# import re

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
        self.assertEqual(calculate_total_score("5/"), 10)
    
    def test_result_of_open_frame(self):
        self.assertEqual(calculate_total_score("45"), 9)

    def test_result_of_two_frames(self):
        self.assertEqual(calculate_total_score('12 12'), 6)
    
    def test_result_of_ten_frames(self):
        self.assertEqual(calculate_total_score('11 11 11 11 11 11 11 11 11 11'), 20)
    
    # def test_result_of_strike_plus_frame(self):
    #     self.assertEqual(calculate_total_score('X 12'), 16)
    

def calculate_total_score(score):
    # lets start it as a list of rolls that are a singular point. then create rules based on that. 
    return 0



if __name__ == '__main__':
    unittest.main()

