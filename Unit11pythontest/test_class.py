import unittest
import AnonymousClass
from Unit11pythontest.AnonymousClass import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """
    def test_store_single_response(self):
        question ="what language did you first learn to speak "
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English',my_survey._responses)
        """
    """
    讲解一下，就直接可以把这个东西声明成我这个class的一个属性，然后每次测试之前，这个setup都会自动运行一下
    """
    def setUp(self):
        question = "what language did you first learn to speak?"
        self.my_survey=AnonymousSurvey(question)
        self.responses=['English','Spanish','Mandarin']

    def test_store_multiple_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey._responses)



if __name__ == '__main__':
    unittest.main()
