import os
import pandas as pd
from typing import List, Dict, Any

class BankReconciler:
    """
    Core logic for reconciling bank statements against internal accounting records.
    """
    def __init__(self):
        self.bank_df = None
        self.ledger_df = None

    def load_data(self, bank_file_path: str, ledger_file_path: str):
        """Load bank statement and internal ledger."""
        # Handle both CSV and Excel
        self.bank_df = self._read_file(bank_file_path)
        self.ledger_df = self._read_file(ledger_file_path)
        print("Data loaded successfully.")

    def _read_file(self, path: str) -> pd.DataFrame:
        if path.endswith('.csv'):
            return pd.read_csv(path)
        elif path.endswith(('.xls', '.xlsx')):
            return pd.read_excel(path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Excel.")

    def reconcile(self, amount_col: str, date_col: str, ref_col: str = None):
        """
        Perform a basic reconciliation.
        Returns matched and unmatched transactions.
        """
        # Normalize columns for comparison
        bank = self.bank_df.copy()
        ledger = self.ledger_df.copy()
        
        # Basic matching logic: Match by exact amount and reference (if provided)
        # In a real scenario, we would implement 'fuzzy matching' for dates or references.
        
        matched_bank = []
        unmatched_bank = []
        unmatched_ledger = []

        for idx, bank_row in bank.iterrows():
            # Find match in ledger
            match = ledger[
                (ledger[amount_col] == bank_row[amount_col]) & 
                (ledger[date_col] == bank_row[date_col])
            ]
            if ref_col and not match.empty:
                match = match[match[ref_col] == bank_row[ref_col]]

            if not match.empty:
                matched_bank.append(bank_row.to_dict())
                ledger = ledger.drop(match.index[0]) # Remove matched row from ledger
            else:
                unmatched_bank.append(bank_row.to_dict())

        unmatched_ledger = ledger.to_dict('records')
        
        return {
            "matched": matched_bank,
            "unmatched_bank": unmatched_bank,
            "unmatched_ledger": unmatched_ledger
        }

    def suggest_entries(self, unmatched_bank: List[Dict]):
        """Suggest accounting entries for unmatched bank transactions."""
        suggestions = []
        for tx in unmatched_bank:
            amount = tx.get('Amount', 'Unknown')
            desc = tx.get('Description', 'No description')
            suggestions.append({
                "transaction": desc,
                "amount": amount,
                "suggested_entry": "Debit: Expense Account / Credit: Bank Account (Pending Verification)"
            })
        return suggestions

# --- Framework Integration (FastAPI/Flask style for AgentBase) ---
# For a real AgentBase deployment, you would wrap this in a GreenNodeAgentBaseApp
if __name__ == "__main__":
    print("Bank Reconciliation Engine initialized.")
    # Example usage:
    # rec = BankReconciler()
    # rec.load_data("bank.csv", "ledger.csv")
    # results = rec.reconcile("Amount", "Date")
    # print(results)
