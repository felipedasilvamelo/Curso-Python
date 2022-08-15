import pygame
#tem funcionalidades para criar jogos, carregar imagens videos e etc..
pygame.init()
pygame.mixer.music.load('ex021.mp3.m4a')
pygame.mixer.music.play()
input()
pygame.event.wait()
#não funcionou porque o pycharm não reconhece como musica
#PESQUISAR DEPOIS COMO RESOLVER ISSO