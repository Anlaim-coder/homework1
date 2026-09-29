string=str(input())

dict_symbols=dict()
for symbol in string:
    if symbol in dict_symbols:
        dict_symbols[symbol]+=1
    else:
        dict_symbols[symbol]=1

top3_symbols=sorted(dict_symbols.items(), key=lambda x: x[1], reverse=True)[:3]

print("Top 3 symbols:")
for symbol in top3_symbols:
    print(symbol[0])
