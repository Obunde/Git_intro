#!/usr/bin/env python
# coding: utf-8

# #Calculating Efficiency of Fuel Depot

# In[56]:


#defining KPI function
def calculate_efficiency(actual_output,target_output):
    if target_output == 0:
        return 0
    efficiency = actual_output/target_output * 100
    return round( efficiency,2)


# In[57]:


def get_operational_status(efficiency):
    if efficiency < 70:
        return "critical"
    elif 70 <= efficiency <90:
        return "warning"
    else:
        return "normal"


# In[ ]:


# Site Data
depots = {
"Nairobi Depot":{
    "actual_output":800,
    "target_output":1000
    },
"Nakuru Depot":{
    "actual_output":400,
    "target_output":1000
    },
"Mombasa Depot":{
    "actual_output":100,
    "target_output":1000
    }
}


# In[59]:


# Looping through each depot to calculate efficiency and status
for depot, data in depots.items():
    actual = data["actual_output"]
    target = data["target_output"]
    efficiency = calculate_efficiency(actual, target)
    status = get_operational_status(efficiency)

    # Pick an emoji based on status, for quick visual scanning
    if status == "critical":
        status_emoji = "🔴"
    elif status == "warning":
        status_emoji = "🟡"
    else:
        status_emoji = "🟢"

    print(f"Depot Name : {depot}")
    print(f"Actual Output  = {actual}")
    print(f"Target Output  = {target}")
    print(f"Efficiency     = {efficiency}%")
    print(f"  {status_emoji} Status         : {status}")
    print()  # blank line between depots


# In[ ]:




