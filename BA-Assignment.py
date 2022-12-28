import pandas as pd
import numpy as np

## Problem Statement -2 
user_signup = pd.read_csv("/content/drive/MyDrive/GreedyGame Assignment/Q2_users signup.csv")

user_offer = pd.read_csv("/content/drive/MyDrive/GreedyGame Assignment/Q2_User offer data.csv")
user_offer = user_offer.drop(['Unnamed: 0'],axis=1)

offer_completion = pd.read_csv("/content/drive/MyDrive/GreedyGame Assignment/Q2_User offer completion data.csv")
offer_completion = offer_completion.drop(['Unnamed: 0'],axis=1)

rewards = pd.read_csv("/content/drive/MyDrive/GreedyGame Assignment/Q2_rewards details.csv")
rewards = rewards.drop(['Unnamed: 0'],axis=1)

a = pd.merge(user_signup,user_offer)
a['offer_status'] = a.status.apply(lambda x: 1 if x=='COMPLETED' else 0)

offers = a.groupby('app_id').agg(offers_initiated = ('offer_status',lambda x: x.eq(0).sum()),
                                        unique_users = ('user_id',pd.Series.nunique)).reset_index()

b = pd.merge(offer_completion,rewards)
rewards_earned = b.groupby('app_id').agg(offer_completion = ('offer_id','count'),
                                         rewards_amount = ('total_payout_in_paise','sum'),
                                         revenue = ('total_revenue_in_paise','sum')).reset_index()

final = pd.merge(offers,rewards_earned)
final['initiated_completion'] = round((final.offer_completion / final.offers_initiated)*100,2)

final
