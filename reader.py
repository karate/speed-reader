
# Import a library of functions called 'pygame'
import pygame
from time import sleep

# Initialize the game engine
pygame.init()

def get_delay(wordsPerMinute):
  return 60/wordsPerMinute

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
  wpm = 200
  delay = get_delay(wpm)

  # Basic colors
  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)

  # Create screen
  screen = pygame.display.set_mode(window_size)
  pygame.display.set_caption("Speed reader")

  # Select the font to use, size, bold, italics
  font = pygame.font.SysFont('Calibri', 40, False, False)
   
  # Clear the screen to white
  screen.fill(WHITE)

  # Loop until the user clicks the close button.
  done = False
   
  # Used to manage how fast the screen updates
  clock = pygame.time.Clock()
   
  # -------- Main Program Loop -----------
  while not done:
      # --- Main event loop
      for event in pygame.event.get():  # User did something
          if event.type == pygame.QUIT: # If user clicked close
              done = True               # Flag that we are done so we exit this loop
   
      # --- Game logic should go here
      
      # Go a little bit faster each time
      delay = delay-0.001
      # Get next word or quit
      try:
        word = words.__next__()
      except StopIteration:
        done = True
        continue

      text = font.render(word, True, BLACK)
      # double the delay if the word end with a full-stop
      if word[-1] == '.':
        frame_delay = delay * 2
      else:
        frame_delay = delay

      # Calculate text position
      text_position = text.get_rect(center=(window_size[0]/2, window_size[1]/2))
      
      # --- Drawing code should go here
      
      # Clear screen
      screen.fill(WHITE)
      
      # Add text to screen
      screen.blit(text, text_position)
      
      # Redraw screen
      pygame.display.flip()

      # Add some delay
      #  print(str(int(60/delay)) + 'wpm')
      sleep(frame_delay)
   
      # Limit to 30 frames per second
      clock.tick(30)
main()