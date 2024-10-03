class Tv:


    def tv_is_on(self):
        return self.is_on
    #end

    def turn_on(self):
        self.is_on = True
    #end

    def turn_off(self):
        self.is_on = False
    #end


    def tv_is_off(self, message):
        if not self.is_on:
            raise ValueError(message)

    def get_channel(self):
        Tv.tv_is_off(self, "Invalid can not get channel when Tv is off!")
        return self.channel
    #end

    def channel_up(self):
        if 0 < self.channel <  100:
            self.channel += 1
        else: self.channel = 1
    #end

    def channel_down(self):
        if 1 > self.channel < 101:
            self.channel -= 1
        else: self.channel = 1
    #end


    def set_channel(self, channel):
        if 1 < channel < 101:
            self.channel = channel
        else: self.channel = 1
    #end

    def get_volume(self):
        Tv.tv_is_off(self, "Invalid can not get volume when Tv is off!")
        if self.muted:
            return 0
        return self.volume_level
    # end

    def volume_up(self):
        if 0 >= self.volume_level <= 10:
            self.volume_level += 1
        else:
            self.volume_level = self.volume_level
        # end

    def volume_down(self):
        if 0 < self.volume_level < 11:
            self.volume_level -= 1
        else:
            self.volume_level = self.volume_level
        # end

    def set_volume(self, volume):
        if 0 <= volume < 11:
            self.volume_level = volume
        else:
            self.volume_level = 0
    # end

    def is_muted(self):
        Tv.tv_is_off(self, "Invalid can mute when Tv is off!")
        return  self.muted

    def mute(self):
        self.muted = not self.muted







    def __init__(self):
        self.channel = 1
        self.volume_level = 0
        self.is_on = False
        self.muted = False
    #end






