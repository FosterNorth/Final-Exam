def coin_to_dollars(sentence):
    # Laying out our excepted words for coins to convert
    coin_values = {
        "penny": 0.01, "pennies": 0.01,
        "nickel": 0.05, "nickels": 0.05,
        "dime": 0.10, "dimes": 0.10,
        "quarter": 0.25, "quarters": 0.25
    }

    total = 0.0

    # splitting the sentence
    sentence = sentence.lower().strip()
    coin_groups = sentence.split(" and ")

    for group in coin_groups:
        parts = group.strip().split()
        if len(parts) == 2:
            quantity_str, coin_type = parts
            try:
                quantity = int(quantity_str)
                if coin_type in coin_values:
                    total += quantity * coin_values[coin_type]
            except ValueError:
                continue

    return round(total, 2)


# Runs the script
if __name__ == "__main__":
    user_input = input("Enter your coins to be added up!")
    result = coin_to_dollars(user_input)
    print(f"Total: ${result}")

   


