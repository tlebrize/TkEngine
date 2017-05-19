import pyglet
from resources.window import TkWindow
from resources.world import TkWorld
from resources.menu import TkMenu

class AboutMenu(TkMenu):

	def __init__(self, world):
		self.label = "About Menu"
		self.menu_items = {
			"ABOUT WHAT LOL ??"	: self.quit,
			"back"			: self.back,
		}
		super(AboutMenu, self).__init__(world)

	def quit(self):
		self._quit()

	def back(self):
		self.world.transition("main")

class MainMenu(TkMenu):

	def __init__(self, world):
		self.label = "Main Menu"
		self.menu_items = {
			"Start"		: self.start,
			"About"		: self.about,
			"Quit"		: self.quit
		}
		super(MainMenu, self).__init__(world)

	def start(self):
		print("start")

	def about(self):
		self.world.transition("about")

	def quit(self):
		self._quit()


def main():
	window = TkWindow(800, 600, visible=False, caption="TESTMENULOL", style="dialog")
	world = TkWorld(window)
	about = AboutMenu(world)
	main = MainMenu(world)
	world.add_scenes({"main": main, "about": about})
	world.transition("main")
	pyglet.app.run()

if __name__ == "__main__":
	main()