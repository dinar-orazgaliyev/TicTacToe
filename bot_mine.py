

class tic_bot():

	def __init__(self):
		#self.SCREEN = SCREEN
		self.player_mark = 'X'
		self.bot_mark = 'O'
		self.board = {0: ' ', 1: ' ', 2: ' ',
         3: ' ', 4: ' ', 5: ' ',
         6: ' ', 7: ' ', 8: ' '}
	
		#self.player_move = True
		

	def is_full(self):

		if ' ' in self.board:
			return False
		return True

	def check_for_win(self):

		if (self.board[0] + self.board[1] + self.board[2] == 3*self.board[0] and self.board[0]!=' '):
			return True
		elif (self.board[3] + self.board[4] + self.board[5] == 3*self.board[3] and self.board[3]!=' '):
			return True
		elif (self.board[6] + self.board[7] + self.board[8] == 3*self.board[6] and self.board[6]!=' '):
			return True
		elif (self.board[0] + self.board[3] + self.board[6] == 3*self.board[0] and self.board[0]!=' '):
			return True
		elif (self.board[1] + self.board[4] + self.board[7] == 3*self.board[1] and self.board[1]!=' '):
			return True
		elif (self.board[2] + self.board[5] + self.board[8] == 3*self.board[2] and self.board[2]!=' '):
			return True
		elif (self.board[0] + self.board[4] + self.board[8] == 3*self.board[0] and self.board[0]!=' '):
			return True
		elif (self.board[2] + self.board[4] + self.board[6] == 3*self.board[2] and self.board[2]!=' '):
			return True
		else:
			return False
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

	def result(self):
		pass


	def player_move(self,i):

		self.board[i] = self.player_mark
		#self.printBoard()
	
	def cmd_move(self):
		move = input()
		self.board[int(move)] = self.player_mark
		#print(self.board)


	def bot_plays(self):
		bestScore = -1000
		bestMove = 0


		for i in self.board.keys():
			print("Check recursion")
			if self.board[i] == ' ':
				self.board[i] = self.bot_mark
				score = self.minimax(False)
				self.board[i] = ' '

				if (score > bestScore):
					bestScore = score
					bestMove = i
		self.board[bestMove] = self.bot_mark
		#print(self.board)
		return bestMove

	def minimax(self,isMaximizing):
		player_won = self.win_check(self.bot_mark)
		bot_won = self.win_check(self.player_mark) 
		isfull = self.is_full()
		if player_won:
			return 100

		elif bot_won:
			return -100
		elif not player_won and not bot_won and isfull:
			return 0

		if isMaximizing:
			bestScore = -1000
			for i in self.board.keys():
				if self.board[i] == ' ':
					self.board[i] = self.bot_mark
					score = self.minimax(False)
					self.board[i] = ' '

					if (score > bestScore):
						bestScore = score
			return bestScore

		else:
			bestScore = 1000
			for i in self.board.keys():
				if self.board[i] == ' ':
					self.board[i] = self.player_mark
					score = self.minimax(True)
					self.board[i] = ' '
					if (score < bestScore):
						bestScore = score
			return bestScore



	def printBoard(self):
	    print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
	    print('-+-+-')
	    print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
	    print('-+-+-')
	    print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])
	    print("\n")


	'''
	def maximizer(self):
		x_bool = self.win_check('X')
		o_bool = self.win_check('O')
		isend = self.is_full()
		maxv = -2
		px = None
		py = None
		if x_bool == False and o_bool == False and isend == True:
			return (0,1,0)
		if x_bool == True:
			return (1,0,0)
		elif o_bool == True:
			return (0,0,-1)
		else:
			return (0,0,0)



		for i in range(1,10):
			if self.board[i] == ' ':
				self.board[i] == 'O'
				(m, min_i, min_j) = self.mininimizer()
				print(m)
				if m > self.maxv:
					self.maxv = m
					min_i = px
					min_j = pv
				self.board[i] = ' '
		#print(m,min_i,min_j)
		return (m,min_i,min_j)



	def mininimizer(self):
		x_bool = self.win_check('X')
		o_bool = self.win_check('O')
		isend = self.is_full()

		minv = 2

		qx = None
		qy = None

		if x_bool == False and o_bool == False and isend == True:
			return (0,1,0)
		if x_bool == True:
			return (1,0,0)
		elif o_bool == True:
			return (0,0,-1)
		else:
			return (0,0,0)


		for i in range(1,10):
			if self.board[i] == ' ':
				self.board[i] == 'X'
				(m, max_i, max_j) = self.maximizer()
				if m < self.minv:
					self.minv = m
					max_i = px
					max_j = pv
				self.board[i] = ' '

		#print(m,max_i,max_j)
		return (m,max_i,max_j)
	'''
	
if __name__ == "__main__":
	bot = tic_bot()
	
	#print(bot.board)
	#print("CHECK")
	#print(bot.check_for_win())
	while not bot.check_for_win():
		#print("LOOP CHECK")
		bot.printBoard()
		bot.cmd_move()
		print(bot.board)
		bot.bot_plays()
		print(bot.board)

	bot.printBoard()

