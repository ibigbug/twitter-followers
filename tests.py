yesterday = ['a', 'b', 'c']
today = ['c', 'd', 'e']

from storage import save_friends, get_diff

save_friends('yesterday', yesterday)
save_friends('today', today)

print(get_diff('yesterday', 'today'))
print(get_diff('today', 'yesterday'))
