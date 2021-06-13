import pygame
import time
import bot_mine
import pdb

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
SCREEN.fill(WHITE)


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
		self.board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
		self.Players = {'X':'','O':''}
		self.Buttons = []

	def draw_grid(self,WINDOW_WIDTH,WINDOW_HEIGHT):
		blockSize = WINDOW_HEIGHT // 3
		#SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
		#pygame.display.flip()

		#self.SCREEN.fill(BLACK)
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

		pygame.draw.line(self.SCREEN,BLUE,[self.Buttons[i].x,self.Buttons[i].y],[self.Buttons[i].x+self.Buttons[i].width,self.Buttons[i].y+self.Buttons[i].height],2)
		pygame.draw.line(self.SCREEN,BLUE,[self.Buttons[i].x,self.Buttons[i].y+self.Buttons[i].height],[self.Buttons[i].x+self.Buttons[i].width,self.Buttons[i].y],2)


	def draw_circle(self,i):
		x = self.Buttons[i].x + 65
		y = self.Buttons[i].y + 65
		pygame.draw.circle(self.SCREEN,BLUE,(x,y),50,3)

	def is_full(self):
		isfull = True
		for i in range(0,9):
			if self.board[i] == ' ':
				isfull = False
		return isfull

	def win_check(self, mark):
		if (self.board[0] + self.board[1] + self.board[2] == 3*mark):
			return True
		elif (self.board[3] + self.board[4] + self.board[5] == 3*mark):
			return True
		elif (self.board[6] + self.board[7] + self.board[8] == 3*mark):
			return True
		elif (self.board[0] + self.board[3] + self.board[6] == 3*mark):
			return True
		elif (self.board[1] + self.board[4] + self.board[7] == 3*mark):
			return True
		elif (self.board[2] + self.board[5] + self.board[8] == 3*mark):
			return True
		elif (self.board[0] + self.board[4] + self.board[8] == 3*mark):
			return True
		elif (self.board[2] + self.board[4] + self.board[6] == 3*mark):
			return True
		else:
			return False





def text_objects(text, font):
	textSurface = font.render(text, True, BLACK)
	return textSurface, textSurface.get_rect()


def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',30)
	TextSurf, TextRect = text_objects(text, largeText)
	TextRect.center = ((WINDOW_WIDTH/2),(WINDOW_HEIGHT/6))
	SCREEN.fill(WHITE)
	SCREEN.blit(TextSurf, TextRect)

	pygame.display.update()

	#time.sleep(2)

def game_loop_single():
	gameExit = False
	tictactoe = TicTacToe(SCREEN)
	tictactoe.draw_grid(WINDOW_WIDTH,WINDOW_HEIGHT)
	bot_move = False
	bot = bot_mine.tic_bot()
	while not gameExit:
		#pdb.set_trace()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_game()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for i in range(0,len(tictactoe.Buttons)):
					if tictactoe.Buttons[i].isOver(pos) and bot_move == False:
						if tictactoe.board[i] == ' ':
							tictactoe.board[i]	 = 'X'
							tictactoe.draw_x(i)
							bot.player_move(i)
							bot_move = True
						if tictactoe.win_check('X') == True:
							pygame.display.flip()
							message_display("X has won")
							time.sleep(1)
							SCREEN.fill(WHITE)
							gameExit = True
						if bot_move == True:
							j = bot.bot_plays()
							#bot.printBoard()
							tictactoe.board[j] = 'O'
							tictactoe.draw_circle(j)
							bot_move = False
							#print("BOTMOVEFALSE")
							time.sleep(2)
							if tictactoe.win_check('O') == True:

									pygame.display.flip()
									message_display("O has won")
									#print("CHECK")
									time.sleep(1)
									SCREEN.fill(WHITE)
									gameExit = True

		if tictactoe.is_full() == True:
					message_display("Draw!")
					time.sleep(1)
					SCREEN.fill(WHITE)
					gameExit = True



		pygame.display.update()
		clock.tick(60)


def game_loop():
	gameExit = False
	tictactoe = TicTacToe(SCREEN)
	tictactoe.draw_grid(WINDOW_WIDTH,WINDOW_HEIGHT)
	is_X = True
	while not gameExit:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit_game()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for i in range(0,len(tictactoe.Buttons)):
					if tictactoe.Buttons[i].isOver(pos) and is_X == True:
						
						if tictactoe.board[i] in ['X','O']:
							print(tictactoe.board[i])
							continue
						elif tictactoe.board[i] == ' ':
							tictactoe.board[i] = 'X'
							tictactoe.draw_x(i)
						is_X = False
						if tictactoe.win_check('X') == True:
							pygame.display.flip()
							message_display("X has won")
							time.sleep(1)
							SCREEN.fill(WHITE)
							gameExit = True


						
					elif tictactoe.Buttons[i].isOver(pos) and is_X == False:
						if tictactoe.board[i] in ['X','O']:
							continue
						elif tictactoe.board[i] == ' ':
							tictactoe.board[i] = 'O'
							tictactoe.draw_circle(i)
						is_X = True
						if tictactoe.win_check('O') == True:
							#pygame.display.flip()
							message_display("O has won")
							time.sleep(1)
							SCREEN.fill(WHITE)
							gameExit = True

				if tictactoe.is_full() == True:
					message_display("Draw!")
					time.sleep(1)
					SCREEN.fill(WHITE)
					gameExit = True
						
						
		pygame.display.update()
		clock.tick(60)


def quit_game():
	pygame.quit()
	quit()


def game_intro():

	intro = True
	#SCREEN.fill(WHITE)
	while intro:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				quit_game()
				
		
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

		greenButton.isCLicked(pos,game_loop_single)
		greenButton2.isCLicked(pos,game_loop)
		greenButton3.isCLicked(pos,quit_game)
		pygame.display.update()
		clock.tick(15)


				









if __name__=="__main__":
	game_intro()
	#game_loop()