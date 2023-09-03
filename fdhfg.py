while True:  
    from gtts import gTTS
    import os
    metin = input("") 
    seslendirme = gTTS(text=metin, lang='tr')
    seslendirme.save("sesli_metin.mp3")
    os.system("sesli_metin.mp3")
