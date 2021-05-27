import pygame

WINDOW_WIDTH = 390 
WINDOW_HEIGHT = 390
FPS = 30
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
CLOCK = pygame.time.Clock()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0,255,255)


class Game:

	def menu_screen():
		pass

	def game():
		pass


class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('Arial', 30)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


def main():
	global SCREEN, CLOCK
	pygame.init()
	#pygame.mixer.init()
	
	running = True
	cyanButton = button(CYAN,90,90,230,90,'2 Players')
	cyanButton.draw(SCREEN,(0,0,0))
	pygame.display.update()
	while running:
		pygame.time.delay(100)
		CLOCK.tick(FPS)
		for event in pygame.event.get():
			pos = pygame.mouse.get_pos()
			

			if event.type == pygame.QUIT:
				running = False
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if cyanButton.isOver(pos):
					#draw_grid()
					print("HELLO")
					draw_grid()
					pygame.display.flip()
			'''
			if event.type == pygame.MOUSEMOTION:
				if cyanButton.isOver(pos):
					cyanButton.color = GREEN
					print("MOTION")
				else:
					cyanButton.color = CYAN
			'''

		SCREEN.fill(BLACK)
		#pygame.display.flip()
		#draw_grid()
		
		#pygame.display.update()

def draw_grid():
	blockSize = 130
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(SCREEN, WHITE, rect, 1)




if __name__=="__main__":
	main()