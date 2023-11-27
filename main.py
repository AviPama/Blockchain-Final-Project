from blockchain import Blockchain

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class AuthenticatedBlockchain(Blockchain):
    def __init__(self):
        super().__init__()
        self.current_user = None

    def login(self, username, password):
        for user in users:
            if user.username == username and user.password == password:
                self.current_user = user
                return True
        return False

    def add_new_movement(self, product_id, movement_details):
        if not self.current_user:
            raise Exception("User not authenticated.")
        super().add_new_movement(product_id, movement_details, self.current_user)

    def logout(self):
        self.current_user = None

class CLIAuthenticatedBlockchain(AuthenticatedBlockchain):
    def handle_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if self.login(username, password):
            print("Login successful.")
        else:
            print("Login failed.")

    def handle_add_movement(self):
        if not self.current_user:
            print("You need to be logged in to add a product movement.")
            return
        product_id = input("Enter product ID: ")
        movement_details = input("Enter movement details: ")
        self.add_new_movement(product_id, movement_details)
        print(f"Movement for {product_id} added.")

    def handle_view_history(self):
        product_id = input("Enter product ID to view history: ")
        history = self.get_product_history(product_id)
        if history:
            print(f"History for {product_id}:")
            for movement in history:
                for block in self.chain:
                    if movement in block.product_movements:
                        print(f"Block Hash: {block.hash}")
                        print("Movement Details:", movement)
                        break
        else:
            print("No history found for this product.")

    def run(self):
        while True:
            print("\n1: Login\n2: Add Product Movement\n3: View Product History\n4: Logout\n5: Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.handle_login()
            elif choice == '2':
                self.handle_add_movement()
            elif choice == '3':
                self.handle_view_history()
            elif choice == '4':
                self.logout()
                print("Logged out.")
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid choice. Please try again.")

# List of users (for demonstration purposes)
users = [User("user1", "password1"), User("user2", "password2")]

if __name__ == "__main__":
    cli_blockchain = CLIAuthenticatedBlockchain()
    cli_blockchain.run()
