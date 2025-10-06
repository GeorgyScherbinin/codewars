class BatmanQuotes(object):
    @staticmethod
    def get_quote(quotes, hero):
        print(hero)
        quote_position = 0
        if hero[0] == "R":
            hero = "Robin"
            quote_position = 1
        if hero[0] == "B":
            hero = "Batman"
            quote_position = 0
        if hero[0] == "J":
            hero = "Joker"
            quote_position = 2
        return hero + ": " + quotes[quote_position]
   
quotes = ["WHERE IS SHE?!", "Holy haberdashery, Batman!", "Let's put a smile on that faaaceee!"]

test_quote = BatmanQuotes.get_quote(quotes, "Rob1n")

print(test_quote)


    
    