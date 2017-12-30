
import pygame
import requests
pygame.mixer.init()

def DameTemperatura():
	# obten la temperatura de internet
	url = "http://api.openweathermap.org/data/2.5/forecast?lat=19.43&lon=-99.177&appid=5cdd2e951fbaedb44576f5e53d85fd16"
	r = requests.get(url)
	mexJSON =  r.json()
	tKelvin = mexJSON["list"][0]['main']['temp']
	tCelsius = tKelvin - 273.15
	return tCelsius

def Duplica(numero1, numero2):
	return numero1*2+numero2



def DameCancionApropiada2(temperatura):
	# si la temperatura es menor a 10 c, quiero que regrese "frozen.mp3"
	if temperatura < 10:
		return "frozen.mp3"
	# si la temperatura esta entre 10 y 20, que regrese "starwarstheme.mp3"
	elif temperatura <= 20:
		return "underthesea.mp3"
	# si la temperatura es mayor a 20 c, quiero que regrese "cumbia.mp3"
	else:
		return "cumbia.mp3"

def PonCancion(temperatura):
	if temperatura < 10:
		pygame.mixer.music.load("frozen.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
	elif temperatura <= 20:
		pygame.mixer.music.load("underthesea.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
	else:
		pygame.mixer.music.load("cumbia.mp3")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue 

def PonCancion2(temperatura):
	if temperatura < 10:
		pygame.mixer.music.load("frozen.mp3")
	elif temperatura <= 20:
		pygame.mixer.music.load("underthesea.mp3")
	else:
		pygame.mixer.music.load("cumbia.mp3")

	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue 

def PonCancion3(cancion):
	pygame.mixer.music.load(cancion)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue



temperatura = DameTemperatura()
print temperatura
cancion = DameCancionApropiada2(temperatura)
print "Va poner cancion "+ cancion
PonCancion3(cancion)
# PonCancion2(15)
# print(DameCancionApropiada2(7))
# print(DameCancionApropiada2(12))
# print(DameCancionApropiada2(23))
