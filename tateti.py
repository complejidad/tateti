import pygame
import random
reloj = pygame.time.Clock()
white=(255,255,255)
black=(0,0,0)
largo=100
alto=100
margen=15
pygame.init()
size=360,360
Screen=pygame.display.set_mode(size)
pygame.display.set_caption("Tateti")

def elegirsimbolo():
	pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 0 + margen,330,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 1 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 2 + margen,largo,alto])
	mens="Eliga su simbolo"
	mensaje=pygame.font.Font(None,50).render(mens, 1, black)
	Screen.blit(mensaje,(50,50))
	mostrarsimbolo(1,1,1)
	mostrarsimbolo(2,1,2)
	b=False
	while b==False:
		evento=pygame.event.wait()
		if evento.type == pygame.QUIT:
			b=True
		elif evento.type == pygame.MOUSEBUTTONDOWN:
			pos=pygame.mouse.get_pos()
			columna = pos[0] // (largo + margen+margen/2)
			fila = pos[1] // (alto + margen+margen/2)
			if columna==1 and fila==1:
				return (1,2)
				b=True
			elif columna==1 and fila==2:
				return (2,1)
				b=True
		reloj.tick(60)
		pygame.display.flip()

def retricula():
	pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 0 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 1 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 2 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 0 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 1 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 2 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 2 + margen, (margen+alto) * 0 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 2 + margen, (margen+alto) * 1 + margen,largo,alto])
	pygame.draw.rect(Screen,white,[(margen+largo) * 2 + margen, (margen+alto) * 2 + margen,largo,alto])

def Gano(m,l):
	return ((m[0][0]==l and m[0][1]==l and m[0][2]==l)
		or (m[1][0]==l and m[1][1]==l and m[1][2]==l)
		or (m[2][0]==l and m[2][1]==l and m[2][2]==l)
		or (m[0][0]==l and m[1][0]==l and m[2][0]==l)
		or (m[0][1]==l and m[1][1]==l and m[2][1]==l)
		or (m[0][2]==l and m[1][2]==l and m[2][2]==l)
		or (m[0][0]==l and m[1][1]==l and m[2][2]==l)
		or (m[0][2]==l and m[1][1]==l and m[2][0]==l))

def obtenerjugada (m,f,c,l):
	if m[f][c]==0:
		m[f][c]=l
		mostrarsimbolo(f,c,l)
		b=True
	else:
		b=False
	return (m,b)

def mostrarsimbolo(fila,columna,letra):
	if letra==1:
		pygame.draw.line(Screen,black,((margen+alto) * columna+margen,(margen+largo) * fila+margen),((margen+alto) * columna+100+margen,(margen+largo) * fila+100+margen),30)
		pygame.draw.line(Screen,black,((margen+alto) * columna+100+margen,(margen+largo) * fila+margen),((margen+alto) * columna+margen,(margen+largo) * fila+100+margen),30)
	elif letra==2:
		pygame.draw.circle(Screen,black,((margen+alto) * columna+50+margen,(margen+largo) * fila+50+margen),50,0)
		pygame.draw.circle(Screen,white,((margen+alto) * columna+50+margen,(margen+largo) * fila+50+margen),25,0)
	

def mostrarmensaje (mens):
	#mens='Juego Terminado!'
	mensaje=pygame.font.Font(None,50).render(mens, 1, black)
	Surface=pygame.Surface((330,100))
	Surface.fill(white)
	Screen.blit(Surface,(15,130))
	Screen.blit(mensaje,(80,165))

def obteneresquina(m):
	e=[]
	if m[0][0]==0:
		e.append([0,0])
	elif m[0][2]==0:
		e.append([0,2])
	elif m[2][0]==0:
		e.append([2,0])
	elif m[2][2]==0:
		e.append([2,2])
	if len(e) != 0:
		return random.choice(e)
	else:
		return None

def obtenerlado(m):
	lado=[]
	if m[0][1]==0:
		lado.append([0,1])
	elif m[1][0]==0:
		lado.append([1,0])
	elif m[1][2]==0:
		lado.append([1,2])
	elif m[2][1]==0:
		ladp.append([2,1])
	if len(lado) != 0:
		return random.choice(lado)
	else:
		return None

def obtenerjugadapc (m,lc,lh):
	c=[]
	#Si hay posibilidad de ganar	
	for i in range(0,3):
		for j in range(0,3):
			c=m
			if c[i][j]==0:
				c[i][j]=lc
				if Gano(c,lc):
					mostrarsimbolo(i,j,lc)
					return(c)
				else:
					c[i][j]=0
	#Si el humano esta por ganar
	for i in range (0,3):
		for j in range (0,3):
			c=m
			if c[i][j]==0:
				c[i][j]=lh
				if Gano(c,lh):
					c[i][j]=lc
					mostrarsimbolo(i,j,lc)
					return(c)
				else:
					c[i][j]=0
	#Ocupar centro
	if m[1][1]==0:
		m[1][1]=lc
		mostrarsimbolo(1,1,lc)
		return (m)

	#Evitar truco 1
	if (m[0][0]==lh and m[2][2]==lh) or (m[0][2]==lh and m[2][0]==lh):
		la=obtenerlado(m)	
		m[la[0]][la[1]]=lc
		mostrarsimbolo(la[0],la[1],lc)
		return(m)

	#Evitar truco 2
	if (m[0][1]==lh and m[1][0]==lh):
		if m[0][0]==0:
			m[0][0]=lc
			mostrarsimbolo(0,0,lc)
			return(m)
	elif(m[0][1]==lh and m[1][2]==lh): 
		if m[0][2]==0:
			m[0][2]=lc
			mostrarsimbolo(0,2,lc)
			return(m)
	elif(m[1][0]==lh and m[2][1]==lh):
		if m[2][0]==0:
			m[2][0]=lc
			mostrarsimbolo(2,0,lc)
			return(m)
	elif(m[1][2]==lh and m[2][1]==lh):
		if m[2][2]==0:
			m[2][2]=lc
			mostrarsimbolo(2,2,lc)
			return(m)
	
	#Ocupar esquina
	e=obteneresquina(m)
	if e!=None:
		m[e[0]][e[1]]=lc
		mostrarsimbolo(e[0],e[1],lc)
		return(m)

	#Ocupar lado
	la=obtenerlado(m)	
	m[la[0]][la[1]]=lc
	mostrarsimbolo(la[0],la[1],lc)
	return(m)

grid=[[0,0,0],[0,0,0],[0,0,0]]
salir= False
lh,lc=elegirsimbolo()
Screen.fill(black)
retricula()
juegoencurso=True
while not salir:
	c=0
	while juegoencurso and not salir:
		evento=pygame.event.wait()
		if evento.type == pygame.QUIT:
			salir=True
		elif evento.type == pygame.MOUSEBUTTONDOWN:
			c=c+1
			b=False
			while b==False:
				# El usuario presiona el raton. Obtiene su posicion.
				pos=pygame.mouse.get_pos()
				# Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
				columna = pos[0] // (largo + margen+margen/2)
				fila = pos[1] // (alto + margen+margen/2)
				grid,b=obtenerjugada(grid,fila,columna,lh)
				if b==False:
					evento=pygame.event.wait()
					while evento.type != pygame.MOUSEBUTTONDOWN:
						evento=pygame.event.wait()
			if ((c>4) and (Gano(grid,lh)==True)):
				mostrarmensaje('Gano humano')
				juegoencurso=False
			c=c+1
			#JugadaPC	
			#grid=obtenerjugada(grid,fila,columna,2)
			if juegoencurso==True and c<10:
				grid=obtenerjugadapc(grid,lc,lh)
				if ((c>4) and (Gano(grid,lc)==True)):
					mostrarmensaje('Gano PC')
					juegoencurso=False
				#Caso empate
			if c>=9:
				mostrarmensaje('   Empate!!')
				juegoencurso=False
		reloj.tick(60)
		pygame.display.flip()
	evento=pygame.event.wait()
	if evento.type == pygame.MOUSEBUTTONDOWN:
		salir=True
pygame.quit()
