import pygame
import pygame.locals
import os
import sys
import random

pygame.init()
#pygame.init() initializes each of the modules in pygame.

sizewd=720#display screen width
sizeht=480#display screen height
HW=720/2
HH=480/2
WHITE=(255,255,255)
mindist=280

win=pygame.display.set_mode((sizewd,sizeht))
clock=pygame.time.Clock()
bg=pygame.image.load(os.path.join("sprites","ground.png"))

pygame.display.set_caption("dino")#caption for the dispaly screen

win.fill((255,255,255))

FPS=40

centre_handle=0
index=0
speed=8

				



class dino:
	def __init__(self,filename,col):
		self.sheet=pygame.image.load(filename)
		self.col=col
	   
		#self.row=row
		#self.totcellcount=row*col
		self.rect=self.sheet.get_rect()
		w=self.cellwidth=self.rect.width/col
		h=self.cellheight=self.rect.height
		hw,hh=self.cellcentre=(w/2,h/2)

		self.cell=list([(index%col*w,0,w,h)for index in range(self.col)])
		
		self.jumping=False
		self.running=True
		self.ducking=False
		
		self.jumpcount=0
		self.con=0
		self.keydown=0
		self.timelapsed=0
	

	   
		self.handle=list([(0,0),(-hw,0),(-w,0),(0,-hh),(-hw,hh),(w,-hh),(0,-h),(-hw,h),(w,-h)])

	def run(self,surface,cellindex,x,y,handle=0):
		surface.blit(self.sheet,(x+self.handle[handle][0],y+self.handle[handle][1]),self.cell[cellindex%4])
		pygame.display.update(x+self.handle[handle][0],y+self.handle[handle][1],self.cellwidth,self.cellheight)
		
	def jump(self,surface,x,y,cellindex):
		
		surface.blit(self.sheet,(x+self.handle[0][0],y+self.handle[0][1]),self.cell[cellindex])    
		pygame.display.update(x+self.handle[0][0],y+self.handle[0][1],self.cellwidth,self.cellheight)

	def duck(self,surface,filename,index):
		self.img=pygame.image.load(filename)

		cw=self.img.get_rect().width/2
		ch=self.img.get_rect().height
		surface.blit(self.img,(120,HH),(index*cw,0,cw,ch))
		pygame.display.update(120,HH,cw,ch)	
	def redraw(self,surface,index):
		rel=(index*-speed)%1203
		surface.fill(WHITE) 
		surface.blit(bg,(rel-1203,HH+75),(0,0,bg.get_rect().width,bg.get_rect().height ))
		if rel<sizewd: 
			surface.blit(bg,(rel,HH+75),(0,0,bg.get_rect().width,bg.get_rect().height ))  
	def events(self):
		for eve in pygame.event.get():
			if eve.type==pygame.QUIT:
				pygame.quit()#uninitialise all pygame modules
				sys.exit()
			#_________________________________DETECTING JUMP button PRESSES_______________________________________
			if eve.type==pygame.locals.KEYDOWN and eve.key==pygame.K_UP and not self.jumping:
				self.keydown=pygame.time.get_ticks()
			if  eve.type==pygame.locals.KEYUP and eve.key==pygame.K_UP and not self.jumping:
				self.timelapsed=pygame.time.get_ticks()-self.keydown
				pygame.event.set_blocked(pygame.locals.KEYDOWN)

				# print(self.timelapsed)
				if(self.timelapsed<=100):
					self.jumpcount=11
				elif self.timelapsed>100 :
					self.jumpcount=13
				self.con=self.jumpcount	
				self.jumping=True

			#__________________________________DETECTING DUCK button PRESSES______________________________________
			if eve.type==pygame.locals.KEYDOWN and eve.key==pygame.K_DOWN :
				s.ducking=True

				# if self.jumpcount>=-self.con:
	   #              neg=0.5
	   #              if self.jumpcount<0:
	   #                  neg=-0.5
	   #              self.y-=(self.jumpcount**2)*0.5*neg
	   #              self.jumpcount-=1
				# 	self.con=self.jumpcount	
				# 	self.jump(win,120,self.HH,1)		            
class objects():
	def __init__(self,x=0):
		self.cact=pygame.image.load(os.path.join("sprites","cacti-small.png"))
		self.cactrect=self.cact.get_rect()
		self.cactwi=self.cactrect.width/6
		self.cacthe=self.cactrect.height
		# self.cactcell=list([(i*self.cactwi,0,self.cactwi,self.cacthe) for i in range(0,6)])
		self.cactcell=list([(0,0,self.cactwi,self.cacthe),(self.cactwi,0,2*self.cactwi,self.cacthe),(3*self.cactwi,0,3*self.cactwi,self.cacthe)])
#y coordinate for spawning cactcell spite= (HH+22)
#y coordinate for spawning CACTcell spite= (HH+7)
		self.xcoordinate=sizewd+x
		self.CACT=pygame.image.load(os.path.join("sprites","cacti-big.png"))
		self.CACTrect=self.CACT.get_rect()
		self.CACTwi=50
		self.CACThe=self.CACTrect.height
		self.CACTcell=list([(0,0,self.CACTwi,self.CACThe),(50,0,100,self.CACThe),(150,0,50,self.CACThe),(200,0,50,self.CACThe)])
		self.Rand=random.randint(0,5)
	def draw(self,surface):
		self.xcoordinate+=-speed
		
		# print(self.xcoordinate)
		if self.Rand<3:
			surface.blit(self.CACT,(self.xcoordinate-self.CACTwi,HH-7),self.CACTcell[self.Rand])			
		else:
			surface.blit(self.cact,(self.xcoordinate-self.cactwi,HH+22),self.cactcell[self.Rand%3])
		
o1=objects()
o2=objects(random.randint(250,350))

s=dino(os.path.join("sprites","dino.png"),5)
y=HH
duckc=[0,1]
i=1
run=True
while run:
			clock.tick(50)
	
			s.events()

			key=pygame.key.get_pressed() 
			if not s.jumping and not s.ducking:
				if s.running:
					s.run(win,index%s.col,120,HH,centre_handle)
				# if key[pygame.K_DOWN]:#DUCKKING
				# 	s.ducking=True
				# 	s.running=False

				# elif key[pygame.K_SPACE] or key[pygame.K_UP]:
				# 	s.jumping=True
				# 	s.running=False  
			elif s.ducking:
				
				if(i%2==0)and not key[pygame.K_DOWN]:
					s.ducking=False
					s.running=True
					s.duck(win,os.path.join("sprites","dino_ducking.png"),i%2)	
				else:
					s.duck(win,os.path.join("sprites","dino_ducking.png"),i%2)
				i+=1			
				
			elif s.jumping :
			
				if s.jumpcount>=-s.con:
					neg=0.4
					if s.jumpcount<0:
						neg=-0.4
					y-=(s.jumpcount**2)*0.5*neg
					s.jump(win,120,y,index%4)
					s.jumpcount-=1
				if s.jumpcount<-s.con:
					s.jumping=False
					
					y=HH
					pygame.event.set_allowed(pygame.locals.KEYDOWN)
					# win.blit(o.CACT,(120+s.cellwidth,HH-7),o.cell[2])			
			# win.blit(o.cact,(120+s.cellwidth,HH+22),o.cactcell[2])
			pygame.display.update()
			s.redraw(win,index)
			
			o1.draw(win)
			
			o2.draw(win)
		
			if(o1.xcoordinate<=0):
				o1.Rand=random.randint(0,6)
				o1.xcoordinate=sizewd
			if(o2.xcoordinate<=0):
				o2.Rand=random.randint(0,6)
				o2.xcoordinate=sizewd+random.randint(250,350)	
			index+=1
		
	
	
