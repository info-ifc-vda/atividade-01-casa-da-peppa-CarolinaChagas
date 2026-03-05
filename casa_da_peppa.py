import glfw 
from OpenGL.GL import * 

def init():
    glClearColor(0,0,1,0)#cor de fundo da janela

def render():
    glClear(GL_COLOR_BUFFER_BIT) #limpa o buffer de cor
    
    glBegin(GL_QUADS) #inicia a construção de um retângulo
    glColor3f(0,1,0) #cor verde - grama 
    glVertex2f(-1,-0.5)
    glVertex2f(-1,-1)
    glVertex2f(1,-1)
    glVertex2f(1,-0.5)
    glEnd() #finaliza 
    
    #casa amarela 
    glBegin(GL_QUADS) 
    glColor3f(1,0.8,0) 
    glVertex2f(-0.4,-0.5)
    glVertex2f(-0.4,0.1)
    glVertex2f(0.4,0.1)
    glVertex2f(0.4,-0.5)
    glEnd()
    
    #telhado
    glBegin(GL_TRIANGLES)
    glColor3f(1,0,0) 
    glVertex2f(-0.4,0.1)
    glVertex2f(0.4,0.1)
    glVertex2f(0,0.4)
    glEnd()

    #porta  (red, green, blue)
    glBegin(GL_QUADS) 
    glColor3f(0.5,0.2,0) 
    glVertex2f(-0.07,-0.5) #x,y
    glVertex2f(-0.07,-0.2)
    glVertex2f(0.07,-0.2)
    glVertex2f(0.07,-0.5)
    glEnd()
    
    #janela 1 - DIREITA
    glBegin(GL_QUADS) 
    glColor3f(0,0.9,1) 
    glVertex2f(0.17,-0.15)   # canto inferior esquerdo
    glVertex2f(0.17,0.04)   # canto superior esquerdo
    glVertex2f(0.3,0.04)   # canto superior direito
    glVertex2f(0.3,-0.15)   # canto inferior direito
    glEnd()
    
    #janela 2 - ESQUERDA
    glBegin(GL_QUADS) 
    glColor3f(0,0.9,1) 
    glVertex2f(-0.30,-0.15)   # canto inferior esquerdo
    glVertex2f(-0.30,0.04)    # canto superior esquerdo
    glVertex2f(-0.17,0.04)    # canto superior direito
    glVertex2f(-0.17,-0.15)   # canto inferior direito
    glEnd()

def main():
    glfw.init() #inicializa a biblioteca glfw
    window = glfw.create_window(800,600, "Casa da Peppa no OpenGL/GLFW", None, None) #monitor e tela compartilhadas (none , none)
    glfw.make_context_current(window) #cria o contexto
    
    init()
    
    while not glfw.window_should_close(window): #roda enquanto não fecha a janela
        glfw.poll_events() #captura eventos
        render()

        glfw.swap_buffers(window) #trabalha com dois buffers
    glfw.terminate()

if __name__ == "__main__":
    main()
