from init_game import *

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # PULO DO PERSONAGEM:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            obj1_y -= (velocidade * 10) # pula

    screen.fill((0, 0, 0))

    ##########
    obj1 = pygame.draw.rect(screen, obj1_color, (obj1_x, obj1_y, obj1_dimensoes_quadrado, obj1_dimensoes_quadrado))
    obj2 = pygame.draw.rect(screen, obj2_color, (obj2_x, obj2_y, obj2_dimensoes_quadrado, obj2_dimensoes_quadrado))
    piso = pygame.draw.rect(screen, piso_color, (piso_x, piso_y, piso_width, piso_height))

    # "GRAVIDADE":
    if obj1_y < (heigth - obj1_dimensoes_quadrado - piso_height):
        obj1_y += (velocidade//2)

    # CONTROLES DO PERSONAGEM:
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_w] and obj1_y > 0:
    #     obj1_y -= velocidade
    if keys[pygame.K_s] and obj1_y < (heigth - obj1_dimensoes_quadrado - piso_height): # if keys[pygame.K_s] and obj1_y < heigth - obj1_dimensoes_quadrado:
        obj1_y += velocidade
    if keys[pygame.K_a] and obj1_x > 0:
        obj1_x -= velocidade
    if keys[pygame.K_d] and obj1_x < width - obj1_dimensoes_quadrado:
        obj1_x += velocidade

    if obj1.colliderect(obj2):
        obj2_hp -= 10
        if obj2_hp <= 0:
            running = False
        obj1_x = random.randrange(10, width - obj1_dimensoes_quadrado)
        obj1_y = random.randrange(10, heigth - obj1_dimensoes_quadrado)
    ##########

    pygame.display.flip()
    clock.tick(60)

pygame.quit()