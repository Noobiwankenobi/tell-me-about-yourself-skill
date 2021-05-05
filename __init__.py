from mycroft import MycroftSkill, intent_file_handler


class TellMeAboutYourself(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('yourself.about.me.tell.intent')
    def handle_yourself_about_me_tell(self, message):
        self.speak_dialog('yourself.about.me.tell')


def create_skill():
    return TellMeAboutYourself()

