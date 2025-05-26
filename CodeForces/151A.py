
n_friends,k_bottles,l_mililiters,c_limes,d_slice,p_grams_salt,nl_mililiters,np_grams =map(int,input().split())


total_toasts_mililiters = int((k_bottles*l_mililiters)/ nl_mililiters)
total_toasts_limes = int(c_limes * d_slice)
total_toasts_salt =int(p_grams_salt/np_grams)


if total_toasts_mililiters < total_toasts_limes and total_toasts_mililiters < total_toasts_salt:
    print(int(total_toasts_mililiters / n_friends))
elif total_toasts_limes < total_toasts_mililiters and total_toasts_limes < total_toasts_salt:
    print(int(total_toasts_limes/n_friends))
else:
    print(int(total_toasts_salt/n_friends))