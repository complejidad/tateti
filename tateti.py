import pygame
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

pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 0 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 1 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 0 + margen, (margen+alto) * 2 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 0 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 1 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 1 + margen, (margen+alto) * 2 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 2 + margen, (margen+alto) * 0 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 2 + margen, (margen+alto) * 1 + margen,largo,alto])
pygame.draw.rect(Screen,white,[(margen+largo) * 2 + margen, (margen+alto) * 2 + margen,largo,alto])
grid=[[0,0,0],[0,0,0],[0,0,0]]
salir= False

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
	if l==1:
		pygame.draw.line(Screen,black,((margen+alto) * c+margen,(margen+largo) * f+margen),((margen+alto) * c+100+margen,(margen+largo) * f+100+margen),30)
		pygame.draw.line(Screen,black,((margen+alto) * c+100+margen,(margen+largo) * f+margen),((margen+alto) * c+margen,(margen+largo) * f+100+margen),30)
	elif l==2:
		pygame.draw.circle(Screen,black,((margen+alto) * c+50+margen,(margen+largo) * f+50+margen),50,0)
		pygame.draw.circle(Screen,white,((margen+alto) * c+50+margen,(margen+largo) * f+50+margen),25,0)
	return (m)

def mostrarmensaje (mens):
	#mens='Juego Terminado!'
	mensaje=pygame.font.Font(None,50).render(mens, 1, black)
	Surface=pygame.Surface((330,100))
	Surface.fill(white)
	Screen.blit(Surface,(15,130))
	Screen.blit(mensaje,(80,165))

juegoencurso=True
while not salir:
	c=0
	#for evento in pygame.event.get():
	while juegoencurso and not salir:
		evento=pygame.event.wait()
		if evento.type == pygame.QUIT:
			salir=True
		elif evento.type == pygame.MOUSEBUTTONDOWN:
			c=c+1
			# El usuario presiona el raton. Obtiene su posicion.
			pos=pygame.mouse.get_pos()
			# Cambia las coordenadas x/y de la pantalla por coordenadas reticulares
			columna = pos[0] // (largo + margen+margen/2)
			fila = pos[1] // (alto + margen+margen/2)
			# Establece esa ubicacion a cero
			if c % 2 !=0:
				grid=obtenerjugada(grid,fila,columna,1)
				if ((c>4) and (Gano(grid,1)==True)):
					mostrarmensaje('Gano cruz')
					juegoencurso=False
			else:
				grid=obtenerjugada(grid,fila,columna,2)
				if ((c>4) and (Gano(grid,2)==True)):
					mostrarmensaje('Gano circulo')
					juegoencurso=False
			if c>=9:
				mostrarmensaje('   Empate!!')
				juegoencurso=False
			print("Click ", pos, "Coordenadas de la reticula: ", fila, columna)
			print (grid)
		reloj.tick(60)
		pygame.display.flip()
	evento=pygame.event.wait()
	if evento.type == pygame.MOUSEBUTTONDOWN:
		salir=True
pygame.quit()
