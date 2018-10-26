import pygame
from time import *
from curses.ascii import isdigit
from nltk.corpus import cmudict
import pyttsx3
engine = pyttsx3.init();
d = cmudict.dict()
def nsyl(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]


pygame.init()
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Bounce")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

info = pygame.display.Info()
sw = info.current_w
sh = info.current_h
y = 0
windowSurface.fill(WHITE)
pygame.draw.circle(windowSurface, YELLOW, (250, 200), 80, 0)
pygame.draw.circle(windowSurface, BLACK, (280, 170), 10, 0)
pygame.draw.circle(windowSurface, BLACK, (220, 170), 10, 0)
pygame.draw.ellipse(windowSurface, BLACK, (225, 230, 50, 10), 0)
myfont = pygame.font.SysFont("ComicSans", 35)
pygame.display.update()

def face(text):
    phrase = text
    pygame.draw.ellipse(windowSurface,BLACK,(225,230,50,10),0)
    myfont = pygame.font.SysFont("ComicSans", 35)
    pygame.display.update()
    sleep(1)
    paragraph =  phrase
    workingSentence = ""
    sleep(0.26)
    for phrase in paragraph.split("?"):
      for sentence in phrase.split("."):
        for word in sentence.split():
          windowSurface.fill(WHITE)
          pygame.draw.circle(windowSurface, YELLOW, (250, 200), 80, 0)
          pygame.draw.circle(windowSurface, BLACK, (280, 170), 10, 0)
          pygame.draw.circle(windowSurface, BLACK, (220, 170), 10, 0)

          pygame.draw.ellipse(windowSurface, BLACK, (225, 220, 50, 30), 0)
          myfont = pygame.font.SysFont("ComicSans", 17)
          workingSentence += word + " "
          label = myfont.render(workingSentence, 1, BLACK)
          windowSurface.blit(label, (5, 5))
          pygame.display.update()
          sleep(0.1)
          engine.say(word);
          engine.runAndWait();
          windowSurface.fill(WHITE)
          pygame.draw.circle(windowSurface, YELLOW, (250, 200), 80, 0)
          pygame.draw.circle(windowSurface, BLACK, (280, 170), 10, 0)
          pygame.draw.circle(windowSurface, BLACK, (220, 170), 10, 0)

          pygame.draw.ellipse(windowSurface, BLACK, (225, 230, 50, 10), 0)
          myfont = pygame.font.SysFont("ComicSans", 17)
          label = myfont.render(workingSentence, 1, BLACK)
          windowSurface.blit(label, (5, 5))
          pygame.display.update()
        windowSurface.fill(WHITE)
        pygame.draw.circle(windowSurface, YELLOW, (250, 200), 80, 0)
        pygame.draw.circle(windowSurface, BLACK, (280, 170), 10, 0)
        pygame.draw.circle(windowSurface, BLACK, (220, 170), 10, 0)

        pygame.draw.ellipse(windowSurface, BLACK, (225, 230, 50, 10), 0)
        myfont = pygame.font.SysFont("ComicSans", 17)
        label = myfont.render(workingSentence, 1, BLACK)
        windowSurface.blit(label, (5, 5))
        pygame.display.update()
