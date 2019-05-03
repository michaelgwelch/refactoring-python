class Performance:
    def __init__(self, aPlayID, anAudience):
        self.playID = aPlayID
        self.audience = anAudience
        self. play = ""
        self.amount = 0
        self.volumeCredits = 0

    def __getitem__(self, key):
        if key == "playID":
            return self.playID
        if key == "audience":
            return self.audience
        if key == "play":
            return self.play
        if key == "amount":
            return self.amount
        if key == "volumeCredits":
            return self.volumeCredits
        raise KeyError(key)

    def __setitem__(self, key, value):
        if key == "playID":
            self.playID = value
        elif key == "audience":
            self.audience = value
        elif key == "play":
            self.play = value
        elif key == "amount":
            self.amount = value
        elif key == "volumeCredits":
            self.volumeCredits = value
        else:
            raise KeyError(key)

    @staticmethod
    def decode(dct):
        if ('playID' in dct) & ('audience' in dct):
            return Performance(dct['playID'], dct['audience'])
        return dct