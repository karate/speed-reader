
# Import a library of functions called 'pygame'
import pygame
from time import sleep

class Speeder():
  min_wpm = None
  max_wpm = None
  delay = None
  min_delay = None
  max_delay = None

  def __init__(self, min_wpm, max_wpm):
    self.min_wpm = min_wpm
    self.max_wpm = max_wpm
    self.delay = self.calculate_delay_from_wpm(min_wpm)
    self.min_delay = self.calculate_delay_from_wpm(max_wpm)
    self.max_delay = self.calculate_delay_from_wpm(min_wpm)

  def calculate_delay_from_wpm(self, wordsPerMinute):
    return 60 / wordsPerMinute

  def calculate_wpm_from_delay(self, delay):
    return 60 / delay

  def get_delay(self):
    return self.delay

  def get_wpm(self):
    return self.calculate_wpm_from_delay(self.delay);

  def increase_delay(self):
    if self.delay < self.max_delay:
      self.delay += 0.02

  def decrease_delay(self):
    if self.delay > self.min_delay:
      self.delay -= 0.02

# Initialize the game engine
pygame.init()

def main():

  # get input file
  import sys
  input_file = sys.argv[1];

  file = open(input_file, 'r')        # open file
  text = file.read()                  # read text
  word_list = text.split(' ')         # split words
  words = iter(word_list)             # create iterator

  # Set window size
  window_size = (400, 150)
  # Set speed

  # Basic colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)

  # Create screen
  screen = pygame.display.set_mode(window_size)
  pygame.display.set_caption("Speed reader")

  # Select the font to use, size, bold, italics
  font = pygame.font.SysFont('Calibri', 40, False, False)
  wpm_font = pygame.font.SysFont('Calibri', 15, False, False)
   
  # Clear the screen to white
  screen.fill(WHITE)

  # Loop until the user clicks the close button.
  done = False
   
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()
  
  speeder = Speeder(250, 600)

  # -------- Main Program Loop -----------
  while not done:
      # --- Main event loop
      for event in pygame.event.get():  # User did something
          if event.type == pygame.QUIT: # If user clicked close
              done = True               # Flag that we are done so we exit this loop
   
      # --- Game logic should go here
      
      pressed = pygame.key.get_pressed()
      if pressed[pygame.K_q]:
        done = True
      elif pressed[pygame.K_UP]:
        speeder.decrease_delay()
      elif pressed[pygame.K_DOWN]:
        speeder.increase_delay()

      # Go a little bit faster each time
      # if delay < max_delay:
      #  delay = delay-0.001
      # Get next word or quit
      try:
        word = words.__next__()
      except StopIteration:
        done = True
        continue

      text = font.render(word, True, BLACK)
      # double the delay if the word end with a full-stop
      if word[-1] == '.':
        frame_delay = speeder.get_delay() * 2
      else:
        frame_delay = speeder.get_delay()

      # Calculate text position
      text_position = text.get_rect(center=(window_size[0]/2, window_size[1]/2))
      
      # --- Drawing code should go here
      
      # Clear screen
      screen.fill(WHITE)
      
      # Add text to screen
      screen.blit(text, text_position)

      # Add wpm
      wpm = speeder.get_wpm();
      wpm_text = wpm_font.render(str(int(speeder.get_wpm())) + 'wpm', True, BLACK)
      screen_width = pygame.display.get_surface().get_width()
      screen_height = pygame.display.get_surface().get_height()
      wpm_text_width = wpm_text.get_rect().width
      wpm_text_height = wpm_text.get_rect().height
      wpm_position = (screen_width - wpm_text_width, screen_height - wpm_text_height)
      screen.blit(wpm_text, wpm_position)
      
      # Redraw screen
      pygame.display.flip()

      # Add some delay
      print(str(int(60/frame_delay)) + 'wpm')
      sleep(frame_delay)
   
      # Limit to 30 frames per second
      clock.tick(30)

main()