state=("A",0,0.0)
for n in range(1,5):
    visible="B" if state[0]=="A" else "A"
    state=(visible,n,state[2]+1.0)
    print(state)
