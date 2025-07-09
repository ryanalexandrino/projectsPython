# Faça um programa que abra e reproduza  uma aúdio em MP3

# Importa o módulo de repproduzação de sons
import pygame

#Busca qual aúdio deve ser reproduzido e o reproduz
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Ryan\Downloads\sample-12s.mp3")
pygame.mixer.music.play()

# Espera enquanto o áudio toca
while pygame.mixer.music.get_busy():
    pass
