peiQi_hobby = {"螺狮粉", "臭豆腐", "榴莲", "apple"}

alex_hobby = {"螺狮粉", "臭豆腐", "榴莲", "💩", 'pizza'}

yuan_hobby = {"pizza", "salad", "ice cream", "臭豆腐", "榴莲", }

hobbies = [peiQi_hobby, yuan_hobby, alex_hobby]

# 给peiQi推荐商品
hobbies.remove(peiQi_hobby)

# peiQi_recommend_list = []
# peiQi_recommend_set = {}
# peiQi_recommend_set.add()
peiQi_recommend_set = set()
print(type(peiQi_recommend_set))

for hobby in hobbies:
    # print(hobby)
    """
    {'榴莲', 'pizza', '臭豆腐', 'salad', 'ice cream'}
    {'榴莲', '螺狮粉', 'pizza', '臭豆腐', '💩'}
    """
    if len(peiQi_hobby.intersection(hobby)) >= 2:
        # print(hobby - peiQi_hobby)
        # peiQi_recommend_list.extend(list(hobby - peiQi_hobby))
        peiQi_recommend_set.update(hobby - peiQi_hobby)

print(peiQi_recommend_set)
