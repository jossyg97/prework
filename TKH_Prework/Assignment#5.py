names_list = ["bob", "jimmy", "max b", "bernie", "jordan", "future hendrix"]
odd_names= []
even_names= []
for names in names_list:
    if len(names) %2 ==0:
        even_names.append(names)
    else:
        odd_names.append(names)

#res= [sub.replace([1], 'c')for sub in odd_names]
                  #j
                  #m
#new_odds= []

#for odd in odd_names:
   # new_odd= odd.replace(odd_names[1],"c")
    #new_odds.append(new_odd)
                           
print ("Even list: ", even_names)
print (" Odd List: ", odd_names)
    

