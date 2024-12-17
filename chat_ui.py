
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QHBoxLayout, QLabel, QComboBox
)
import requests

class ChatUI(QWidget):
    interact_with_model = Signal(str)
    update_model_text = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Chat")

        self.layout = QVBoxLayout()
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        input_layout = QHBoxLayout()
        self.input_area = QLineEdit()
        self.input_area.setPlaceholderText("Type your message...")
        input_layout.addWidget(self.input_area)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)

        self.clear_button = QPushButton("Clear Context")
        self.clear_button.clicked.connect(self.clear_context)
        input_layout.addWidget(self.clear_button)

        self.layout.addLayout(input_layout)

        config_layout = QVBoxLayout()
        url_layout = QHBoxLayout()
        url_label = QLabel("API URL:")
        self.api_url_input = QLineEdit("http://your-custom-api-url.com/chat")
        url_layout.addWidget(url_label)
        url_layout.addWidget(self.api_url_input)
        config_layout.addLayout(url_layout)

        key_layout = QHBoxLayout()
        key_label = QLabel("API Key:")
        self.api_key_input = QLineEdit("your-api-key")
        self.api_key_input.setEchoMode(QLineEdit.Password)
        key_layout.addWidget(key_label)
        key_layout.addWidget(self.api_key_input)
        config_layout.addLayout(key_layout)

        model_layout = QHBoxLayout()
        model_label = QLabel("Model:")
        self.model_selector = QComboBox()
        self.model_selector.addItems(["gpt-3.5", "gpt-4", "custom-model-1"])
        model_layout.addWidget(model_label)
        model_layout.addWidget(self.model_selector)
        config_layout.addLayout(model_layout)

        self.layout.addLayout(config_layout)
        self.setLayout(self.layout)

        self.chat_context = [{"role": "system", "content": "You are a helpful assistant."}]

    def send_message(self):
        user_message = self.input_area.text()
        if user_message.strip():
            self.chat_display.append(f"You: {user_message}")
            self.input_area.clear()
            self.chat_context.append({"role": "user", "content": user_message})
            ai_response = self.get_ai_response(user_message)
            self.chat_display.append(f"AI: {ai_response}")
            self.chat_context.append({"role": "assistant", "content": ai_response})
            self.update_model_text.emit(user_message)
            self.trigger_model_animation(user_message)

    def get_ai_response(self, message):
        try:
            model_name = self.model_selector.currentText()
            payload = {
                "model": model_name,
                "messages": self.chat_context
            }
            api_url = self.api_url_input.text()
            api_key = self.api_key_input.text()
            headers = {"Authorization": f"Bearer {api_key}"}
            response = requests.post(api_url, json=payload, headers=headers)
            if response.status_code == 200:
                result = response.json()
                return result.get("reply", "No response from API")
            else:
                return f"Error: API returned status code {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def clear_context(self):
        self.chat_context = [{"role": "system", "content": "You are a helpful assistant."}]
        self.chat_display.clear()
        self.chat_display.append("Chat context cleared. Start a new conversation!")

    def trigger_model_animation(self, message):
        if "hello" in message.lower():
            self.interact_with_model.emit("wave")
        elif "bye" in message.lower():
            self.interact_with_model.emit("sad")
        elif "happy" in message.lower():
            self.interact_with_model.emit("happy")
        else:
            self.interact_with_model.emit("idle")
        