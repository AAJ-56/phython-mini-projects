"""
Convert INR to USD using the live USD→INR rate.
Source (BookMyForex, 13 Aug 2025): 1 USD = 87.47 INR[60].
"""

def convert_inr_to_usd():
    try:
        inr = float(input("Enter amount in INR: "))
        if inr < 0:
            raise ValueError("Amount must be non-negative")
    except ValueError as e:
        print(f"❌ Invalid input: {e}")
        return

    rate = 87.47  # 1 USD = 87.47 INR[60]
    usd = inr / rate
    print(f"{inr:.2f} INR = {usd:.2f} USD")

if __name__ == "__main__":
    convert_inr_to_usd()
