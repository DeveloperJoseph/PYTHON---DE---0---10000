from gtts  import gTTS#import librerias

#Definiendo mi metodo que recibe tres variables
def  method_tts(text_file,language,name_file):
    with open(text_file,"r") as file:#abriendo y leendo nuestro archivo
        text = file.read()#declaramos una variable 'text' para almacenar nuestro archivo leido
    file = gTTS(text=text,lang=language)#nuestra variable 'file' es igual al metodo de nuestra libreria
    filename = name_file
    file.save(filename)

print(">> Loading convert text a voice...")
name_archive = str(input(">> Name of archive (.mp3): "))
method_tts("E:\PYTHON - DE - 0 - 10000\Modulo 1\helloworld.txt","EN","E:\PYTHON - DE - 0 - 10000\Modulo 1\ "+name_archive+".mp3")
print(">> Save.....")
