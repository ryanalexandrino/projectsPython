# Faça um programa que abra e reproduza um aúdio em MP3

# Importa o módulo de reproduzação pygame
import pygame

# Inicia o modulo e o método, busca qual aúdio deve ser reproduzido e o reproduz
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Ryan\Downloads\sample-12s.mp3")
pygame.mixer.music.play()

# Espera enquanto o áudio toca, depois finaliza
while pygame.mixer.music.get_busy():
    pass
