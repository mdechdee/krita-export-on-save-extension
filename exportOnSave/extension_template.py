from krita import *


class ExtensionTemplate(Extension):

    def __init__(self, parent):
        super().__init__(parent)

    def onDocumentSaved(self, filename):
        currentDocument = Krita.instance().activeDocument()

        # setup some export parameters for PNG
        exportParameters = InfoObject()
        exportParameters.setProperty("alpha", True)
        exportParameters.setProperty("compression", 3)
        exportParameters.setProperty("indexed", False)

        currentDocument.setBatchmode(True)
        # exportImage supports jpg and png
        currentDocument.exportImage(filename.removesuffix(
            '.kra').replace('/', '\\') + '.png', exportParameters)
        currentDocument.setBatchmode(False)

    # Krita.instance() exists, so do any setup work

    def setup(self):
        appNotifier = Krita.instance().notifier()
        appNotifier.setActive(True)

        appNotifier.imageSaved.connect(self.onDocumentSaved)

    # called after setup(self)
    def createActions(self, window):
        pass
