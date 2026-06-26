from abc import ABC, abstractmethod

# 1. The Target Interface: What your client expects
class FinancialSystem(ABC):
    @abstractmethod
    def get_balance(self) -> float:
        pass

# 2. The Adaptee: The incompatible legacy/third-party code
class LegacyBankAPI:
    def fetch_available_amount(self) -> dict:
        # Returns a weird format your new system doesn't understand
        return {"currency": "USD", "amount": 15400.50}

# 3. The Adapter: Bridges the gap between LegacyBankAPI and FinancialSystem
class BankAdapter(FinancialSystem):
    def __init__(self, legacy_api: LegacyBankAPI):
        self._legacy_api = legacy_api

    def get_balance(self) -> float:
        # Translate the incompatible response into the expected format
        legacy_data = self._legacy_api.fetch_available_amount()
        return legacy_data["amount"]

# 4. Client Code: Works with any class that adheres to the FinancialSystem interface
def display_account_funds(system: FinancialSystem):
    funds = system.get_balance()
    print(f"Verified Funds: ${funds:,.2f}")

# --- Execution ---
if __name__ == "__main__":
    legacy_api = LegacyBankAPI()
    
    # Adapt the legacy API so it fits your new financial system
    adapter = BankAdapter(legacy_api)
    
    # The client calls get_balance() blindly, unaware it's being adapted
    display_account_funds(adapter)
