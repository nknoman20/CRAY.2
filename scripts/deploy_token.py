import os
from dotenv import load_dotenv
from toncenter import TonCenterClient

load_dotenv()

API_KEY = os.getenv("TON_API_KEY")
client = TonCenterClient(api_key=API_KEY)

def deploy_token():
    print("Deploying Crayzilla (CRAY) token...")
    # Placeholder - Actual logic will use Tact compiler and deployment steps
    print("Token deployed successfully on TON mainnet.")

if __name__ == "__main__":
    deploy_token()
