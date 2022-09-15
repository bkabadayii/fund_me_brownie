from brownie import accounts, FundMe, network, exceptions
import pytest
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")

    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts[1]

    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw(
            {"from": bad_actor, "gas_limit": 6721975, "allow_revert": True}
        )
