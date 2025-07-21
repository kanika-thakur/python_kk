import streamlit as st 
st.title("login box")
firstname=st.text_input("ENTER FIRST NAME:")
lastname=st.text_input("ENTER LAST NAME:")
result=firstname.title()
result1=lastname.title()

if(st.button("sucess")):
   final_result=result+result1
   st.success(final_result)



