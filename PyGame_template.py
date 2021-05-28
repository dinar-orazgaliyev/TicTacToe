import pygame


pygame.init()
WINDOW_WIDTH = 390 
WINDOW_HEIGHT = 390
FPS = 30
SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
CYAN = (0,255,255)




def draw_grid():
	blockSize = 130
	#SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
	#pygame.display.flip()
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(SCREEN, WHITE, rect, 1)
			#print("drawing")

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def game_loop():
	gameExit = False

	while not gameExit:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		#draw_grid()
		#SCREEN.fill(BLACK)
	pygame.display.update()
	clock.tick(15)


def quit_game():
	pygame.quit()
	quit()


def game_intro():

	intro = True

	while intro:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				quit_game()
				
		SCREEN.fill(BLACK)
		largeText = pygame.font.Font('freesansbold.ttf',30)
		TextSurf, TextRect = text_objects("A Tic Tac Toe!!!", largeText)
		TextRect.center = ((WINDOW_WIDTH/2),(WINDOW_HEIGHT/6))
		SCREEN.blit(TextSurf, TextRect)

		pos = pygame.mouse.get_pos()

		greenButton = button(GREEN,120,100,150,40,'1 Player')
		greenButton2 = button(GREEN,120,160,150,40,'2 Players')
		greenButton.draw(SCREEN,(0,0,0))
		greenButton2.draw(SCREEN,(0,0,0))
		greenButton3 = button(GREEN,120,220,150,40,'Quit')
		greenButton3.draw(SCREEN,(0,0,0))
		if greenButton.isOver(pos):
			greenButton.color = BRIGHT_GREEN
			greenButton.draw(SCREEN,(0,0,0))
		elif greenButton2.isOver(pos):
			greenButton2.color = BRIGHT_GREEN
			greenButton2.draw(SCREEN,(0,0,0))
		elif greenButton3.isOver(pos):
			greenButton3.color = BRIGHT_GREEN
			greenButton3.draw(SCREEN,(0,0,0))

		greenButton.isCLicked(pos,game_loop)
		greenButton3.isCLicked(pos,quit_game)
		pygame.display.update()
		clock.tick(15)

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

	def isCLicked(self,pos,action):
		click = pygame.mouse.get_pressed()
		if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
			if click[0] == 1 and action != None:
				print(True)
				action()
				









if __name__=="__main__":
	game_intro()
	#game_loop()