from mycroft import MycroftSkill, intent_file_handler


class AnswerHello(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hello.answer.intent')
    def handle_hello_answer(self, message):
        self.speak_dialog('hello.answer')


def create_skill():
    return AnswerHello()

