# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:29:20 2019
@author: sbyog
"""

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class PythonaSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()
        self.learning = True

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        my_setting = self.settings.get('my_setting')

#    @intent_handler(IntentBuilder('ThankYouIntent').require('YogeshKeyword'))
#    def handle_thank_you_intent(self, message):
#        """ This is an Adapt intent handler, it is triggered by a keyword."""
#        self.speak_dialog("welcome")
#
#    @intent_handler('HowAreYou.intent')
#    def handle_how_are_you_intent(self, message):
#        """ This is a Padatious intent handler.
#        It is triggered using a list of sample phrases."""
#        self.speak_dialog("how.are.you")

    @intent_handler(IntentBuilder('number').require('numberKeyword'))
    def handle_hello_world_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("There are five types of log messages: "
                      "info, debug, warning, error, and exception.")
        self.speak_dialog("number_matching")

    def stop(self):
        pass


def create_skill():
    return PythonaSkill()
