st=input("enter string")
print("original string",st)
a=st[0];
st1=st.replace(a,"$")
st1=st[0]+st1[1:]
print("the new string",st1)