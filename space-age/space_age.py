from __future__ import division

class SpaceAge(object):
  def __init__(self, seconds):
    self.seconds = seconds
    self.solar_system = {
      "on_mercury": 0.2408467,
      "on_venus": 0.61519726,
      "on_mars": 1.8808158,
      "on_jupiter": 11.862615,
      "on_saturn": 29.447498,
      "on_uranus": 84.016846,
      "on_neptune": 164.79132
    }

  def on_earth(self):
    return round(self.seconds / 31557600, 2)

  def __getattr__(self, name):
    def _missing(*args, **kwargs):
      return round(self.seconds / 31557600 / self.solar_system[name], 2)
    return _missing
