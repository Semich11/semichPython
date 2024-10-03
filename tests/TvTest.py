import unittest

from Tv import Tv


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.tv = Tv()
    def test_that_tv_is_off(self):
        is_on = self.tv.tv_is_on()
        self.assertFalse(is_on)

    #end

    def test_that_tv_is_switch_on(self):
        tv = Tv()
        tv.turn_on()
        is_on = tv.tv_is_on()
        self.assertTrue(is_on)

    # end

    def test_that_tv_is_switch_off(self):
        tv = Tv()
        tv.turn_on()
        tv.turn_off()
        is_on = tv.tv_is_on()
        self.assertFalse(is_on)

    # end

    #end
    def test_that_tv_can_get_channel(self):
        tv = Tv()
        tv.turn_on()
        channel = tv.get_channel()
        self.assertEqual(1, channel)

    def test_that_tv_can_not_get_channel_when_tv_is_off(self):
        tv = Tv()
        with self.assertRaises(ValueError):
            tv.get_channel()


    def test_that_tv_can_change_channel_up(self):
        tv = Tv()
        tv.turn_on()
        tv.channel_up()
        self.assertEqual(2, tv.get_channel())

    #endR

    def test_that_tv_can_change_channel_down(self):
        tv = Tv()
        tv.turn_on()
        tv.channel_up()
        tv.channel_down()
        self.assertEqual(1, tv.get_channel())

    #end

    def test_that_tv_can_change_set_channel(self):
        tv = Tv()
        tv.turn_on()
        tv.set_channel(10)
        self.assertEqual(10, tv.get_channel())

    #end

    def test_that_tv_channel_can_not_change_to_a_channel_move_than_channel_100(self):
        tv = Tv()
        tv.turn_on()
        tv.set_channel(100)
        tv.channel_up()
        self.assertEqual(1, tv.get_channel())

    #end

    def test_that_tv_channel_can_not_change_to_a_channel_lower_than_channel_1(self):
        tv = Tv()
        tv.turn_on()
        tv.channel_down()
        self.assertEqual(1, tv.get_channel())
        tv.set_channel(0)
        self.assertEqual(1, tv.get_channel())

    #end

    def test_that_tv_volume_can_not_be_changed_when_tv_is_off(self):
        tv = Tv()
        with self.assertRaises(ValueError):
            tv.get_volume()

    def test_that_tv_can_change_volume_up(self):
        tv = Tv()
        tv.turn_on()
        tv.volume_up()
        self.assertEqual(1, tv.get_volume())

    #endR

    def test_that_tv_can_change_volume_down(self):
        tv = Tv()
        tv.turn_on()
        tv.set_volume(5)
        self.assertEqual(5, tv.get_volume())

        tv.volume_down()
        self.assertEqual(4, tv.get_volume())

    #end

    def test_that_tv_can_set_volume(self):
        tv = Tv()
        tv.turn_on()
        tv.set_volume(5)
        self.assertEqual(5, tv.get_volume())

    #end

    def test_that_tv_volume_can_not_change_to_a_volume_move_than_volume_10(self):
        tv = Tv()
        tv.turn_on()
        tv.set_volume(10)
        tv.volume_up()
        self.assertEqual(10, tv.get_volume())

    #end

    def test_that_tv_volume_can_not_change_to_a_volume_lower_than_volume_1(self):
        tv = Tv()
        tv.turn_on()
        tv.volume_down()
        self.assertEqual(0, tv.get_volume())
        tv.set_volume(-222)
        self.assertEqual(0, tv.get_volume())

    #end

    def test_that_tv_can_get_volume(self):
        tv = Tv()
        tv.turn_on()
        volume = tv.get_volume()
        self.assertEqual(0, volume)
    #end

    def test_that_tv_can_not_be_muted_when_tv_is_off(self):
        tv = Tv()
        with self.assertRaises(ValueError):
            tv.is_muted()
    #end

    def test_that_tv_can_not_be_muted_when_tv_is_on(self):
        tv = Tv()
        with self.assertRaises(ValueError):
            tv.is_muted()

    def test_that_new_tv_is_muted(self):
        tv = Tv()
        tv.turn_on()
        self.assertFalse(tv.is_muted())
    #end

    def test_that_tv_can_mute_when_tv_is_on(self):
        tv = Tv()
        tv.turn_on()
        tv.mute()
        self.assertTrue(tv.is_muted())

    def test_that_volume_is_the_same_when_mute_and_unmute(self):
        self.tv.turn_on()
        self.tv.set_volume(7)
        self.assertEqual(7, self.tv.get_volume())
        self.tv.mute()
        self.assertEqual(0, self.tv.get_volume())




if __name__ == '__main__':
    unittest.main()
