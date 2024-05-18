from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class DecoderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        self.input_label = Label(text='Enter encoded text:')
        self.layout.add_widget(self.input_label)

        self.input_text = TextInput(multiline=False)
        self.layout.add_widget(self.input_text)

        self.decode_button = Button(text='Decode')
        self.decode_button.bind(on_press=self.decode_text)
        self.layout.add_widget(self.decode_button)

        self.result_label = Label(text='Decoded text will appear here.')
        self.layout.add_widget(self.result_label)

        return self.layout

    def decode_from_CT37c(self, encoded_text):
        # Define the decoding dictionary
        decoding_dict = {
            '1': 'A', '2': 'E', '3': 'I', '4': 'N', '5': 'O', '6': 'T',
            '70': 'B', '71': 'C', '72': 'D', '73': 'F', '74': 'G', '75': 'H',
            '76': 'J', '77': 'K', '78': 'L', '79': 'M', '80': 'P', '81': 'Q',
            '82': 'R', '83': 'S', '84': 'U', '85': 'V', '86': 'W', '87': 'X',
            '88': 'Y', '89': 'Z', '91': '.', '92': ':', '93': "'", '94': '()',
            '95': '+', '96': '-', '97': '=', '99': 'SPC'
        }

        # Decode the text
        decoded_text = ''
        i = 0
        while i < len(encoded_text):
            if encoded_text[i] in ['7', '8', '9'] and i + 1 < len(encoded_text):
                code = encoded_text[i:i+2]
                i += 2
            else:
                code = encoded_text[i]
                i += 1

            # Decode the code and add it to the decoded text
            if code in decoding_dict:
                decoded_text += decoding_dict[code]

        return decoded_text

    def decode_text(self, instance):
        encoded_text = self.input_text.text
        decoded_text = self.decode_from_CT37c(encoded_text)
        self.result_label.text = f'Decoded text: {decoded_text}'

if __name__ == '__main__':
    DecoderApp().run()
