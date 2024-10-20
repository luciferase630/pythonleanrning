class AnonymousSurvey():
    def __init__(self,question):
        self._question=question
        self._responses=[]#set to null  zero out
    def show_question(self):
        print(self._question)
    def store_response(self,new_response):
        self._responses.append(new_response)

    def show_results(self):
        print("Survey in response")
        for response in self._responses:
            print(response)
