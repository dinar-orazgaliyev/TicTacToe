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

	def isCLicked(self,pos,action=None):
		click = pygame.mouse.get_pressed()
		if self.x + self.width > pos[0] > self.x and self.y + self.height > pos[1] > self.y:
			if click[0] == 1 and action != None:
				print(True)
				action()

class TicTacToe():


	def __init__(self,SCREEN):
		self.SCREEN = SCREEN
		self.board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
		self.available = [str(num) for num in range(0,10)] # a List Comprehension
		self.Players = {'X':'','O':''}
		self.Buttons = []

	def draw_grid(self,WINDOW_WIDTH,WINDOW_HEIGHT):
		blockSize = WINDOW_HEIGHT // 3
		#SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		pygame.display.flip()

		self.SCREEN.fill(BLACK)
		for x in range(0, WINDOW_WIDTH, blockSize):
			for y in range(0, WINDOW_HEIGHT, blockSize):
				#rect = pygame.Rect(x, y, blockSize, blockSize)
				#pygame.draw.rect(self.SCREEN, WHITE, rect, 1)
				button_tmp = button(WHITE,x,y,blockSize,blockSize)
				button_tmp.draw(self.SCREEN,(0,0,0))
				y = y + blockSize
				self.Buttons.append(button_tmp)

			x = x + blockSize


	def draw_x(self,i):
		pygame.draw.line(self.SCREEN,BLACK,[self.Buttons[i].x,self.Buttons[i].y],[self.Buttons[i].x+self.Buttons[i].width,self.Buttons[i].y+self.Buttons[i].height])
		pygame.draw.line(self.SCREEN,BLACK,[self.Buttons[i].x,self.Buttons[i].y+self.Buttons[i].height],[self.Buttons[i].x+self.Buttons[i].width,self.Buttons[i].y])


	def draw_circle(self):
		pass





def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


def game_loop():
	gameExit = False

	while not gameExit:
		tictactoe = TicTacToe(SCREEN)
		tictactoe.draw_grid(WINDOW_WIDTH,WINDOW_HEIGHT)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_game()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for i in range(0,len(tictactoe.Buttons)):
					if tictactoe.Buttons[i].isOver(pos):
						tictactoe.draw_x(i)
				#tictactoe.Buttons[0].isCLicked(pos,tictactoe.draw_x(0)) 
				#tictactoe.Buttons[8].isCLicked(pos,tictactoe.draw_x(8)) 
		
		
		#print(tictactoe.Buttons[0].x,tictactoe.Buttons[0].y)
		#print(tictactoe.Buttons[0].width,tictactoe.Buttons[0].height)

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
				
		SCREEN.fill(WHITE)
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


				









if __name__=="__main__":
	game_intro()
	#game_loop()