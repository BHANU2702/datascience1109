#!/usr/bin/env python
# coding: utf-8

# In[45]:


def health_premium_quote(gender,dateofbirth,habit):
    if gender=="Male":
        if 1990<dateofbirth<=2000:
            if habit=='Smoker':
                print("Your annual premium is RS 35000")
            elif habit=="Non Smoker":
                print("Your annual premium is RS 35000 but you are eligible for 10% discount on premium")
                Discounted_Premium = 35000-((10/100) * 35000)
                print ("Your final discounted premium is Rs",Discounted_Premium)
        elif 1970<dateofbirth<=1990:
            if habit=='Smoker':
                print("Your annual premium is RS 40000")
            elif habit=="Non Smoker":
                print("Your annual premium is RS 40000 but you are eligible for 5% discount on premium")
                Discounted_Premium = 40000-((5/100) * 40000)
                print ("Your final discounted premium is Rs",Discounted_Premium) 
    elif gender=='Female':
        if 1990<dateofbirth<=2000:
            if habit=='Smoker':
                print("Your annual premium is RS 30000")
            elif habit=="Non Smoker":
                print("Your annual premium is RS 30000 but you are eligible for 10% discount on premium")
                Discounted_Premium = 30000-((10/100) * 30000)
                print ("Your final discounted premium is Rs",Discounted_Premium)
        elif 1970<dateofbirth<=1990:
            if habit=='Smoker':
                print("Your annual premium is RS 35000")
            elif habit=="Non Smoker":
                Discounted_Premium = 35000-((5/100) * 35000)
                print ("Your final discounted premium is Rs",Discounted_Premium) 
        


# In[47]:


health_premium_quote('Male',1990,'Non Smoker')


# In[ ]:




