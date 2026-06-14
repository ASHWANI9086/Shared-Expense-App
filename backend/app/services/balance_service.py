from app.core.db import DB

class BalanceService:

    def compute_balances(self):

        balances = {}

        for exp in DB["expenses"]:
            user = exp.get("paid_by", "unknown")
            amount = exp.get("amount", 0)

            balances[user] = balances.get(user, 0) + amount

        DB["balances"] = balances
        return balances

    def simplify(self):
        # simplified splitwise-style output
        balances = self.compute_balances()

        debtors = []
        creditors = []

        for user, amt in balances.items():
            if amt < 0:
                debtors.append((user, amt))
            else:
                creditors.append((user, amt))

        return {
            "debtors": debtors,
            "creditors": creditors
        }