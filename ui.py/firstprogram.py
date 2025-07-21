# simple program:
# import streamlit as st
# st.title("welcome")
# st.header("Iam KANIKA")
# st.subheader("2005")
# st.text("kannu")
# st.success("Iam good")
# st.warning("warning")
# st.error("error")
# st.ZeroDivisionError("zero division error")


# print name:
import streamlit as st # type: ignore

st.title("login box")
name=st.text_input("enter your name:")
if(st.button("submit")):
    result=name.title()
    st.success(result)