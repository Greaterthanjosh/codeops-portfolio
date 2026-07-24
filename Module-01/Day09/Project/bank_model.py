from collections import deque
from registry import AccountFactory, AccountRegistry


class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.accounts = []

    def add_child(self, branch):
        self.children.append(branch)

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        total = sum(account.balance for account in self.accounts)

        for child in self.children:
            total += child.total_balance()

        return total


def bfs(transfers, start):
    visited = set()
    queue = deque([start])

    while queue:
        current = queue.popleft()

        if current not in visited:
            visited.add(current)

            for neighbor in transfers.get(current, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited


if __name__ == "__main__":

    registry = AccountRegistry()

    acc1 = AccountFactory.create(
        "savings",
        "Eyasu",
        "1003",
        5000
    )

    acc2 = AccountFactory.create(
        "current",
        "Almaz",
        "1001",
        12000
    )

    acc3 = AccountFactory.create(
        "savings",
        "Dawit",
        "1002",
        8000
    )

    acc4 = AccountFactory.create(
        "current",
        "Sara",
        "1004",
        6000
    )

    acc5 = AccountFactory.create(
        "savings",
        "Abel",
        "1005",
        9000
    )

    registry.add(acc1)
    registry.add(acc2)
    registry.add(acc3)
    registry.add(acc4)
    registry.add(acc5)

    head_office = Branch("Head Office")
    north_region = Branch("North Region")
    south_region = Branch("South Region")
    city_branch = Branch("City Branch")
    rural_branch = Branch("Rural Branch")

    head_office.add_child(north_region)
    head_office.add_child(south_region)

    north_region.add_child(city_branch)
    south_region.add_child(rural_branch)

    head_office.add_account(acc2)
    north_region.add_account(acc1)
    city_branch.add_account(acc3)
    rural_branch.add_account(acc4)
    rural_branch.add_account(acc5)

    print("===== BRANCH HIERARCHY =====")
    print(head_office.name)
    print("├──", north_region.name)
    print("│   └──", city_branch.name)
    print("└──", south_region.name)
    print("    └──", rural_branch.name)

    print("\n===== TOTAL BRANCH BALANCE =====")
    print(f"Total Balance: {head_office.total_balance()} ETB")

    transfers = {
        "1001": ["1002", "1003"],
        "1002": ["1004"],
        "1003": ["1005"],
        "1004": [],
        "1005": ["1001"]
    }

    print("\n===== TRANSFERS GRAPH =====")

    for sender, recipients in transfers.items():
        print(f"{sender} -> {recipients}")

    reachable = bfs(transfers, "1001")

    print("\n===== BFS TRAVERSAL =====")
    print("Starting Account: 1001")
    print("Reachable Accounts:", reachable)