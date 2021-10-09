from random import choice


class BGM():
    def __init__(self):
        songs = [
            'Flag', 'Excellent', 'FlagTracker', 'HallofSunrise',
            'NotaGoodbye', 'SpaceField', 'StarlightVocals',
            'Trich', 'WalkThePath', 'Whisper', 'WishingWell', 'Womper',
            'YouMightBeRight'
        ]

        self.music = {}
        for song in songs:
            self.music[song] = base.loader.load_sfx("music/{}.ogg".format(song))

        sfx = [
            'soul-symphony'
        ]
        self.sfx = {}
        for s in sfx:
            self.sfx[s] = base.loader.load_sfx("audio/{}.wav".format(s))

        base.playSfx(self.sfx['soul-symphony'])
        base.playMusic(self.music[choice(songs)], 1, 1, None, 0)
