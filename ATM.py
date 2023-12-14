class ATM
  # constructor(megicaldunder method)
  def __init__(self)
    # for making  datamethod private we can use __ in starting of datamethod 's name (encapsulation)
    self.__pin = " "
    self.__balance = 0
    self.menu()

  # getter(encapsulation)
  def get_pin(self)
    return self.__pin

  #setter(encapsulation)
  def set_pin(self, new_pin)
    self.__pin = new_pin
    print(fyour new pin is {new_pin})

  def menu(self)
    user_input = input(
    hello, please select a option
    1=press 1 for create your pin
    2=press 2 for deposit 
    3=press 3 for withdraw
    4=press 4 for check balance
    5=press 5 for exit
    )
    if user_input == 1
      self.create_pin()
    elif user_input == 2
      self.deposit()
    elif user_input == 3
      self.withdraw()
    elif user_input == 4
      self.check_balance()
    else
      self.exit()

  def create_pin(self)
    self.__pin = input(create your pin)
    print(seccessfully created)

    self.menu()

  def deposit(self)
    confirmation = input(enter your pin)
    if confirmation == self.__pin
      amount = int(input(how much money you want to deposit))
      self.__balance = self.__balance + amount
    else
      print(incorrect pin)

    self.menu()

  def withdraw(self)
    confirmation = input(enter your pin)
    if confirmation == self.__pin
      amount = int(input(how much money you want to withdraw))
      if amount  self.__balance
        self.__balance = self.__balance - amount
        print(withdraw succesfully)
      else
        print(insuficent funds)
    else
      print(incorrect pin)

    self.menu()

  def check_balance(self)
    confirmation = input(enter your pin)
    if confirmation == self.__pin
      print(self.__balance)
    else
      print(incorrect pin)

    self.menu()

  def exit(self)
    print(exit )


BOB = ATM()
