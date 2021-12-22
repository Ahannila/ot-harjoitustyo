from repositories.user_repository import user_repository
from repositories.expense_repository import expense_repository
from database_connection import get_database_connection
from entities.user import User
from entities.expense import Expense

class InvalidCreds(Exception):
    pass

class UserExists(Exception):
    pass


class Budget_calculator():
    def __init__(self):
        self.user = None


    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username (String): Käyttäjän valitsema nimike
            password (String): Käyttäjän valitsema salasana

        Raises:
            InvalidCreds: Heittää kirjautumisruudulle ilmoituksen
            väärästä tunnuksesta.

        Returns:
            User: Käyttäjä-olion
        """
        user = user_repository.find_by_name(username)

        if not user or user.password != password:
            #print('Kirjautuminen ei onnistunut')
            raise InvalidCreds('Invalid username or password')
            
        #print("Kirjautuminen onnistui")
        self.user = user
        return user


    def create_account(self, username, password):
        """Luo käyttäjän

        Args:
            username (String): Käyttäjän nimike
            password (String): Salasana

        Raises:
            InvalidCreds: Jos mitään ei ole syötetti käyttäjäksi
            InvalidCreds: Jos käyttäjätunnus on jo otettu

        Returns:
            User: Palauttaa käyttäjäolion
        """
        user_in_user = user_repository.find_by_name(username)

        if len(str.strip(username)) == 0 or len(str.strip(password)) == 0:
            raise InvalidCreds('Nothing inserted')

        if user_in_user:
            raise InvalidCreds('username taken')

        user = user_repository.create((User(username,password)))
        print("User created")
        return user


    def get_user(self):
        """Palauttaa käyttäjän

        Returns:
            User: User-olio
        """
        return self.user


    def add_budget(self,name,content):
        """Lisää budgetin tietokantaan

        Args:
            name (String): Käyttäjän nimike
            content ([type]): Lisättävän budjetioinni määrä

        Returns:
            Expense: Expense-olion
        """

        if not content:
            return
        if content.isalpha():
            return 
        expense = Expense(self.user.username, name, content)
        expense_repository.add_expense(expense)
        return expense

    def get_expenses(self):
        """Hakee kaikki käyttäjän kulut

        Returns:
            Palauttaa listan kuluista.
        """
        lista = expense_repository.list_expenses(self.user.username)
        return lista
    
    def get_expense_id(self,expense):
        """Palauttaa tulo/menon tunnisteen

        Returns:
            String: tunniste
        """
        id = expense_repository.get_expense_id(self.user.username, expense)
        return id

    def get_expense_name_with_id(self,id):
        """Hakee summan nimen id:n avulla

        Args:
            id: tulo/menon tunniste

        Returns:
            String: tulo/menon nimi
        """
        name = expense_repository.get_expense_name_with_id(id)
        return name


    def get_sum_of_expenses(self):
        """Hakee käyttäjän kaikkien tulo/menojen summan

        Returns:
            String: Summa menoista
        """
        sum = expense_repository.get_sum(self.user.username)
        return sum

    def remove_expense(self, id):
        """Poistaa id:n avulla tulo/menon

        Args:
            id: tulo/menon tunniste
        """
        expense_repository.remove_expense(id)


budget_calculator = Budget_calculator()

