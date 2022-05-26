import pandas as pd
import time

card_df = pd.read_csv('top_gainers.csv')
print(card_df)
print('-------------------')
print('-------------------')

last_num = card_df.iloc[-1][0]
last_num_str = str(int(last_num) + 1)

new_card = [{"Index": last_num_str,
            "Name": "New Card",
            "Set": "New Set",
            "New_Price": "Big money",
            "Old Price": "Small money",
            "PCT": "some percentage",
            }]

new_card_df = pd.DataFrame(new_card)
print(new_card_df)
new_card_df.to_csv("top_gainers.csv", mode='a', index=False, header=False)
