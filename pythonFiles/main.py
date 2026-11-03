from customtkinter import *
from validation import emailValidation
from encryption import passwordEncryption
from database import createAccount, loginHandle, connectToDatabase

window = CTk()
window.geometry("500x400")
window._set_appearance_mode("light")
set_default_color_theme("Oceanix.json") #json file from, https://github.com/avalon60/ctk_theme_builder
window.title("Python Password Encryption GUI with MySql")
window.iconbitmap("data-encryption-pic.ico")

# Database Selection
databaseFrame = CTkFrame(master=window)
databaseFrame.pack(pady=30, padx=30, fill="both", expand=True)

databaseLabel = CTkLabel(
    master=databaseFrame,
    text="Choose Database",
    font=("New York Times", 30)
)
databaseLabel.pack(pady=20)

databaseChoice = StringVar(value="sqlite")

databaseMenu = CTkOptionMenu(
    master=databaseFrame,
    values=["sqlite", "mysql"],
    variable=databaseChoice
)
databaseMenu.pack(pady=15)

def openLoginScreen():

    # Connect to the selected database
    try:
        connectToDatabase(databaseChoice.get())
    except Exception as err:
        print(f"Database connection error: {err}")
        return

    # Hide the database selection screen
    databaseFrame.pack_forget()

    # Original Login GUI
    loginFrame = CTkFrame(master=window, bg_color="black", border_width=2)
    loginFrame.pack(pady=10, padx=30, fill="both", expand=True)

    label = CTkLabel(master=loginFrame, text="Login", font=("New York Times", 40))
    label.pack(pady=12, padx=10)

    emailEntry = CTkEntry(master=loginFrame, placeholder_text="Email")
    emailEntry.pack(pady=12, padx=10)

    passwordEntry = CTkEntry(master=loginFrame, placeholder_text="Password", show="*")
    passwordEntry.pack(pady=12, padx=10)

    loginBtn = CTkButton(
        master=loginFrame,
        bg_color="#51667e",
        text="Login",
        command=lambda: loginHandle(emailEntry, passwordEntry)
    )
    loginBtn.pack(pady=8)

    createAccountButton = CTkButton(
        master=loginFrame,
        bg_color="#51667e",
        text="Create Account",
        command=lambda: createAccount(emailEntry, passwordEntry)
    )
    createAccountButton.pack(pady=8)

continueButton = CTkButton(
    master=databaseFrame,
    text="Continue",
    command=openLoginScreen
)
continueButton.pack(pady=20)

if __name__ == "__main__":
    window.mainloop()
