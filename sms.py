  #biggames
    def Big(self):
        try:
             url = "https://a.postscript.io/v2/back_in_stock/subscribe"
             json = {"product_url":"https://shop.biggames.io/products/santa-monkey-plush","shop_id":"248578","variant_id":"40454491439187","phone_number":{self.phone}}
             r = requests.post(url, json=json)
             if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {self.phone} --> BigGames")
                self.adet += 1
             else:
                 raise
           except:
               print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {self.phone} --> BigGames")
