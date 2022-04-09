print('Annyi szamot olvasunk be...')

nums = [int(input('Addj meg egy szamot:')) for _ in range(int(input('Hany szamot akarsz beadni? ')))]
print(f"""
A megadott szamok: {nums}
A legkisebb megadott szam: {min(nums)}
A legnagyobb megadott szam: {max(nums)}
""")
