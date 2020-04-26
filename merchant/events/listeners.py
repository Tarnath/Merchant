import pygame


class EventTarget:

    def __init__(self):
        self.trigger_action = None


class ClickTarget(EventTarget):

    def check_hit(self, event: pygame.event.Event):
        pass


class EventListener:

    def __init__(self, target: EventTarget):
        self.target = target

    def trigger(self, events):
        pass


class ClickListener(EventListener):

    def __init__(self, target: ClickTarget):
        super().__init__(target)
        self.__valid_types = [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION, pygame.MOUSEWHEEL]

    def trigger(self, events):
        for event in events:
            if self.__valid_types.__contains__(event.type):
                if self.target.check_hit(event):
                    self.target.trigger_action(event.type)
