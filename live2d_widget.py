
from PySide6.QtQuickWidgets import QQuickWidget
from PySide6.QtCore import QUrl, Signal, Slot
from PySide6.QtWidgets import QVBoxLayout, QWidget, QComboBox

class Live2DWidget(QWidget):
    model_changed = Signal(str)
    update_bubble = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Live2D Model")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.model_selector = QComboBox()
        self.model_selector.addItems(["model1", "model2"])
        self.model_selector.currentTextChanged.connect(self.change_model)
        self.layout.addWidget(self.model_selector)

        self.quick_widget = QQuickWidget()
        self.quick_widget.setResizeMode(QQuickWidget.SizeRootObjectToView)
        self.quick_widget.setSource(QUrl("qml/live2d_view.qml"))
        self.layout.addWidget(self.quick_widget)

    @Slot(str)
    def trigger_animation(self, animation_name):
        self.quick_widget.rootObject().triggerAnimation(animation_name)

    def change_model(self, model_name):
        model_path = f"file:///resources/live2d_model/{model_name}/index.html"
        self.model_changed.emit(model_path)
        self.quick_widget.rootObject().loadModel(model_path)
        