from characters.character import Character

class Bullet(Character):

    def __init__(self, position: list, sprite:str,position_change: list, state: str,):
        """
        Initialisation des variables intiales du projet
        """
        super().__init__(position,sprite,position_change)
        self.position_change = position_change
        self.state = state

    def get_state(self):
        """
        Accesseur de la valeur de l'état
        """
        return self.state
    def set_state(self, new_state):
        """
        Mettre la valeur de l'état à un nouvel état
        """
        self.state = new_state

    def fire(self, screen, X, Y):
        """
        Cette fonction permet de tirer une balle du vaisseau lorsque l'état de cette balle est fire
        """

        if self.state == "fire":
            screen.blit(self.load_sprite, (self.get_position[X] + 16, self.get_position[Y] + 10))
            self.get_position[Y] -= self.get_position_change[Y]

    def move_limitations(self, X, Y):
        """
        Cette fonction permet que les balles du vaisseau reste dans le cadre du jeu
        """
        if self.get_position[X] <= 0:
            self.get_position[Y] = 480
            self.set_state("ready")








