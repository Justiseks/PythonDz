class Wallet:
    psystem = "Гемляндия"

    def __init__(self, name: str, currency: str):
        self.name = name
        self.currency = currency
        self._balance = 0

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Баланс кошелька {self.name} пополнен на {amount} {self.currency}")

    def withdraw(self, amount: float):
        if amount > self._balance:
            print("Недостаточно средств на балансе")
        else:
            self._balance -= amount
            print(f"С баланса кошелька {self.name} списано {amount} {self.currency}")

    def balance_info(self):
        print(f"Баланс кошелька {self.name}: {self._balance} {self.currency}")

    def delete_account(self):
        del self

class CryptoWallet(Wallet):
    def __init__(self, name: str, currency: str, coin: str):
        super().__init__(name, currency)
        self.coin = coin

    def balance_info(self):
        print(f"Баланс кошелька {self.name}: {self._balance} {self.coin}")

    def balance_in_usd(self, btc_price: float, eth_price: float):
        if self.coin == "BTC":
            usd_balance = self._balance * btc_price
        elif self.coin == "ETH":
            usd_balance = self._balance * eth_price
        else:
            print("Неподдерживаемая криптовалюта")
            return
        print(f"Баланс кошелька {self.name} в долларах: ${usd_balance:.2f}")


wallet1 = Wallet('"Гемы"', "USD")
wallet1.deposit(8742)
wallet1.balance_info()
wallet1.withdraw(300)
wallet1.balance_info()

crypto_wallet = CryptoWallet('"КриптоГемы"', "BTC", "BTC")
crypto_wallet.deposit(0.0367)
crypto_wallet.balance_info()
crypto_wallet.balance_in_usd(72000, 3500)
crypto_wallet.withdraw(3)
