import pygame

WHITE = (255,255,255)
BLUE = (0, 120, 215)
DARK_BLUE = (0,0,0)

class Button:
    def __init__(self, x, y, width, height, text,
                 font_size= 30, bg_color= BLUE,
                 hover_color= DARK_BLUE, text_color= WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont(None, font_size)
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = self.rect.collidepoint(mouse_pos)
        color = self.hover_color if is_hovered else self.bg_color
        pygame.draw.rect(surface, color, self.rect)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False