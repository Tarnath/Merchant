import pygame
from merchant.events import listeners


class EventHandler:

    def __init__(self):
        self.__listeners = []

    def add_listener(self, listener: listeners.EventListener):
        self.__listeners.append(listener)

    def remove_listener(self, listener: listeners.EventListener):
        self.__listeners.remove(listener)

    def trigger_listeners(self, events):
        for listener in self.__listeners:
            listener.trigger(events)
