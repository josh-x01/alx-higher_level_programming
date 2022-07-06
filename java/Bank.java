class Bank {
	String first_name;
	String last_name;
	static final double INITIAL = 25.00;
	Hashtable<long, double> accounts = new Hashtable();

	void set_account_number(long account) {
		accounts.put(account, 0);
	}

	Bank() {
		this("Not avaliable", "Not avaliable", 0);
	}

	Bank(String fname, String lname, double balance) {
		first_name = fname;
		last_name = lname;
	}

	void view_balance() {
		System.out.println(this.balance);
	}

	int transfer_to_other(Bank transfer_account, double amount) {
		if (balance - INITIAL >= amount) {
			transfer_account.balance += amount;
			balance -= amount;
		}
		else {return -1}
		return 1;
	}

	void deposite(double amount) {
		balance += amount;
	}
	
	int withdraw(double amount) {
		if (balance - INITIAL >= amount) {
			balance -= amount;
		}
		else { return -1}
		return 1;
	}

	int transfer_own_account(long from, long where, double amount) {

		
	
	}


}
