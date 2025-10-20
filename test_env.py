from dotenv import load_dotenv
import os

dotenv_path = r"C:\Users\Admin\Downloads\Sprint1_chatbot\.env"
load_dotenv(dotenv_path=dotenv_path)

token = os.getenv("TELEGRAM_TOKEN")
print("Ruta usada para .env:", dotenv_path)
print("Token encontrado:", token)
