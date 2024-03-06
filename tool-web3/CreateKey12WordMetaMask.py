from eth_account import Account
from thuvien import thuvien
ExcelApp = thuvien.ExcelApp()

Account.enable_unaudited_hdwallet_features()
for i in range (1,6):
    user_data_dir = ExcelApp.read_excel(f'A{i}')
    ExcelApp.save_excel()
    acct, mnemonic = Account.create_with_mnemonic()
    private_key_bytes = acct.key
    private_key_hex = private_key_bytes.hex()
    print('\n---------------------------------------')
    print(acct.key)  
    print("Private Key (hex):", private_key_hex)
    print(mnemonic)
    print(acct.address)
    ExcelApp.write_excel(f'C{i}',private_key_hex)
    ExcelApp.write_excel(f'D{i}',mnemonic)
    ExcelApp.write_excel(f'E{i}',acct.address)
    print(user_data_dir)