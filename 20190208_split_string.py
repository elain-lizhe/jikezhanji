daily_transactions_split = [["a ", " b "], [" c", "d "]]
# expected
#transactions_clean = ["a", "b",  "c", "d" ]
# [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'd']]
# expected
#transactions_clean = [["a", "b"],  ["c", "d" ]]

transactions_clean = []
for m in daily_transactions_split:
    transactions_clean_a = []
    #  transactions_clean_a = []
    # 注意：transactions_clean_a = []，所在位置不同，产生的结果不同。(1)transactions_clean_a = []在for m in daily_transactions_split:循环之外，产生的结果是'green&white&blue', '09/15/17', 'Myrtle Morris', '$22.66', 'green&white&blue', '09/15/17'。（2）
    for n in m:
        transactions_clean_a.append(n.strip())
        # transactions_clean_a.append(n)
    transactions_clean.append(transactions_clean_a)
print(transactions_clean)
