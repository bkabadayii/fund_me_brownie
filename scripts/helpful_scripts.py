from brownie import network, accounts, config, MockV3Aggregator

DECIMALS = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    account = get_account()
    print(f"The active network is {network.show_active()}...")
    print("Deploying mocks...")

    # Deploy MockV3Aggregator
    if len(MockV3Aggregator) <= 0:
        print("Deploying MockV3Aggregator...")
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": account})

    print("Mocks deployed! ")
