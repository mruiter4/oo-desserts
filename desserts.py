"""Dessert classes."""


class Cupcake:
  """A cupcake."""

  cache = {}

  def __repr__(self):
    """Human-readable printout for debugging."""

    return f'<Cupcake name="{self.name}" qty={self.qty}>'

  def __init__(self, name, flavor, price):
    """create a cupcake"""

    self.name = name
    self.flavor = flavor
    self.price = float(price)
    self.qty = 0

    self.cache[name] = self

  def add_stock(self, amount):
    """add the number of cupcakes in amount to the qty"""

    self.qty += amount

  def sell(self, amount):
    """sell the number of cupcakes in amount and adjust qty"""

    if self.qty == 0:
      print('Sorry, these cupcakes are sold out')
      return

    if self.qty < amount:
      self.qty = 0
      return

    self.qty -= amount

  @staticmethod
  def scale_recipe(ingredients, amount):
    """scale each ingredient tuple by value in amount

    tuples are ('ingredient', amount)
    """

    return [(ingredient[0], (ingredient[1] * amount)) 
             for ingredient in ingredients]

  @classmethod
  def get(cls, name):
    """get a cupcake"""

    if name not in cls.cache:
      print("Sorry, that cupcake doesn't exist")
      return

    return cls.cache[name]


class Brownie(Cupcake):
  """Brownie Object"""

  def __init__(self, name, price):
    super().__init__(name, "Chocolate", price)



  if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                          report=False,
                          optionflags=(
                              doctest.REPORT_ONLY_FIRST_FAILURE
                          ))
    doctest.master.summarize(1)
    if result.failed == 0:
      print('ALL TESTS PASSED')
