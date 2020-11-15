import goslate
from gtts import gTTS

test=input("Enter text:")
gs=goslate.Goslate()
language=input("Enter the language:")
trans=gs.translate(test,language)
print(trans)
voice=gTTS(text=trans,lang=language,slow=False)
file_name=input("Enter the file name:")
voice.save(file_name)
