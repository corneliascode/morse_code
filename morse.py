import tkinter as tk
from ttkbootstrap import Style, ttk

############################################################################
# Create the dictionary with morse code & symbols

morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}



#####################################################################

# Function to translate text to morse code
def show_text_to_morse():
    input_text = entry.get().upper() 
    morse_code = []
    for char in input_text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(' ')  # Use space for unknown characters
    morse_text = ' '.join(morse_code)
    print("Input Text:", input_text)
    print("Morse Code:", morse_text)
    morse_code_output_label.config(text="Morse Code: " + morse_text)


# Function to translate morse code to text
def show_morse_code_to_text():
    morse_code = entry1.get().split()  
    decoded_text = []
    for symbol in morse_code:
        for char, code in morse_code_dict.items():
            if code == symbol:
                decoded_text.append(char)
                break
        else:
            decoded_text.append(' ') 
    text = ''.join(decoded_text)
    print("Morse Code:", entry1.get())
    print("Decoded Text:", text)
    text_output_label.config(text="Text: " + text)


##########################################################

# Create the main window
window = tk.Tk()
window.title("Morse Code Translator")
window.geometry("400x400")
style = Style(theme='morph')

# Create home screen
home_frame = ttk.Frame(window, padding="20")
home_frame.pack()

home_label = ttk.Label(home_frame, text="Text to Morse Code", 
                       font=('tk.DefaultFont', 20))
home_label.pack(pady=4)

# Text -> Morse Code button
label = tk.Label(text="Input Text")
entry = tk.Entry()
label.pack()
entry.pack()
b = tk.Button(window, text="Encode", command=show_text_to_morse)  
b.pack()


# Create a Label to display Morse code output
morse_code_output_label = tk.Label(window, text="", font=('tk.DefaultFont', 10))
morse_code_output_label.pack()

# Morse Code button -> Text
home_frame1 = ttk.Frame(window, padding="20")
home_frame1.pack()

home_label1 = ttk.Label(home_frame1, text="Morse Code to Text", 
                       font=('tk.DefaultFont', 20))
home_label1.pack(pady=4)

label1 = tk.Label(text="Input Text")
entry1 = tk.Entry()
label1.pack()
entry1.pack()
c = tk.Button(window, text="Decode", command=show_morse_code_to_text)
c.pack()

# Create a Label to display Text output
text_output_label = tk.Label(window, text="", font=('tk.DefaultFont', 10))
text_output_label.pack()


window.mainloop()
