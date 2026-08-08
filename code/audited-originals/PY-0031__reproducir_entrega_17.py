state='A'; H=set()
for e in range(4):
 state='B' if state=='A' else 'A'; H.add(e); print(state,sorted(H))
