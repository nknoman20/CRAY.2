contract SampleJetton {
    name: "Crayzilla";
    symbol: "CRAY";
    decimals: 9;
    description: "Official Crayzilla Token on TON";
    image: "";
    max_supply: 100000000 * 10^9;
    owner_address: sender();

    init {
        total_supply: 100000000 * 10^9;
        balances[owner_address] = total_supply;
    }

    get_total_supply() => total_supply;
    get_balance(address) => balances[address] or 0;
}
