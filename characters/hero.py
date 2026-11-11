from character import Character

# con
GAME_OVER = "Game over !"
CONTINUE = "Continer le jeu !"

class Hero(Character):

    def __init__(self, positionX: int, positionY: int, sprite: str, characterX_change: int, nombre_vies):
        """
        Initialise les paramètres de la classe Héro
        """
        super().__init__(positionX, positionY, sprite, characterX_change,nombre_vies)


    @property
    def determiner_statut_partie(self):
        """
        Déterminer le statut de la partie en cours
        """
        return  GAME_OVER if self.nombre_vies == 0 else CONTINUE
