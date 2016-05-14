from PyQt4 import QtCore
from PyQt4.QtCore import QObject
from event import Event

class EventManager(QObject):
    controlSignal = QtCore.pyqtSignal(Event)
    displaySignal = QtCore.pyqtSignal(Event)

    def sendControlSignal(self, event):
        self.controlSignal.emit(event)

    def sendDisplaySignal(self, event):
        self.displaySignal.emit(event)

    def listenForControl(self, slot):
        self.controlSignal.connect(slot)

    def listenForDisplay(self, slot):
        self.displaySignal.connect(slot)
