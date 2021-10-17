from random import choice


class BGM():
    def __init__(self):
        self.songs = [
            'Flag', 'Excellent', 'FlagTracker', 'HallofSunrise',
            'NightDrive', 'SpaceField', 'StarlightVocals',
            'Trich', 'WalkThePath', 'Whisper', 'WishingWell', 'Womper',
            'YouMightBeRight', 'The_Spirit_Flag_Instrumental', 'Through_my_Heart_Instrumental', 'Today2'
        ]

        self.music = {}
        for song in self.songs:
            self.music[song] = base.loader.load_sfx("music/{}.ogg".format(song))

        sfx_names = [
            'soul-symphony',
            'correct_guess',
            'incorrect_guess',
        ]
        self.sfx = {}
        for s in sfx_names:
            self.sfx[s] = base.loader.load_sfx("audio/{}.wav".format(s))

        self.current_sfx = self.sfx['soul-symphony']
        #base.playSfx(self.current_sfx)
        self.current_music = self.music[choice(self.songs)]
        #base.playMusic(self.current_music, 1, 1, None, 0)
            
        
    def playMusic(self, track = None, loop = True):
        print(self.current_music.status)
        if track == None:
            track = self.music[choice(self.songs)]
        self.current_music.setLoop(loop)
        self.current_music.play()
        
        
    def stopMusic(self):
        #if (self.current_music.status()== 2):
        self.current_music.stop()
            
    def playSfx(self, sfx = None):
        if sfx == None:
            print("No sfx provided.")
            return
        self.current_sfx = self.sfx[sfx]
        self.current_sfx.play()
        